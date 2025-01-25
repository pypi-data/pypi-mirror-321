import os
import json
from typing import Dict, Any, List, Callable
import requests
from litellm import completion


class LaughingFaceModule:
    """A callable module that can be invoked with dynamic arguments."""
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    def __call__(self, **kwargs) -> str:
        """Invoke the module with dynamic arguments."""
        system_prompt_template = self.config.get("system_prompt", "")
        user_prompt_template = self.config.get("user_prompt", "")
        model_id = self.config.get("model_id", "openai/gpt-4o-mini")
        temperature = self.config.get("temperature", 0.7)

        try:
            system_prompt = system_prompt_template.format(**kwargs)
            user_prompt = user_prompt_template.format(**kwargs)
        except KeyError as e:
            raise ValueError(f"Missing argument for placeholder: {e}")

        try:
            response = completion(
                model=model_id,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=temperature
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            raise RuntimeError(f"Failed to invoke module {self.config.get('module_name', 'unknown')}: {e}")


class LaughingFace:
    def __init__(self, api_key: str = None, base_dir: str = ".laughingface/modules", api_endpoint: str = "https://us-central1-dsports-6ab79.cloudfunctions.net"):
        self.base_dir = base_dir
        self.api_key = api_key or os.getenv("LAUGHINGFACE_API_KEY")
        if not self.api_key:
            raise EnvironmentError("API key is not set. Pass it as an argument or set LAUGHINGFACE_API_KEY in the environment.")
        self.api_endpoint = api_endpoint
        self.ensure_directory()

    def ensure_directory(self):
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

    def fetch_remote_modules(self) -> Dict[str, Any]:
        try:
            url = f"{self.api_endpoint}/get_data"
            headers = {"Content-Type": "application/json"}
            payload = json.dumps({"api_key": self.api_key})

            response = requests.post(url, headers=headers, data=payload)

            print(f"Raw response: {response.text}")

            response.raise_for_status()

            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise RuntimeError(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            raise RuntimeError(f"Request error occurred: {req_err}")
        except ValueError as json_err:
            raise RuntimeError(f"Failed to decode JSON: {json_err}")

    def init(self):
        remote_modules = self.fetch_remote_modules()

        if not isinstance(remote_modules, dict):
            raise RuntimeError(f"Unexpected data structure: {remote_modules}")

        for module_name, config in remote_modules.items():
            self.save_local_module(module_name, config)

    def save_local_module(self, module_name: str, config: Dict[str, Any]):
        config["module_name"] = module_name
        module_path = os.path.join(self.base_dir, f"{module_name}.json")
        with open(module_path, "w") as f:
            json.dump(config, f, indent=4)

    def list_modules(self) -> List[str]:
        return [
            f for f in os.listdir(self.base_dir)
            if os.path.isfile(os.path.join(self.base_dir, f)) and f.endswith(".json")
        ]

    def load_module(self, module_name: str) -> Dict[str, Any]:
        module_path = os.path.join(self.base_dir, f"{module_name}.json")
        if not os.path.exists(module_path):
            raise FileNotFoundError(f"Module {module_name} does not exist")

        with open(module_path, "r") as f:
            return json.load(f)

    def module(self, module_name: str) -> Callable[..., str]:
        config = self.load_module(module_name)
        return LaughingFaceModule(config)
