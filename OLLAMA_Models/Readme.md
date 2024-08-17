# Mistral Model Running

Use "ollama [command] --help" for more information about a command.
welcome@jaisairams-Laptop ~ % ollama list
NAME          	ID          	SIZE  	MODIFIED
llama2:13b    	d475bf4c50bc	7.4 GB	13 days ago
llama2:latest 	78e26419b446	3.8 GB	13 days ago
llama3:latest 	365c0bd3c000	4.7 GB	2 months ago
mistral:latest	61e88e884507	4.1 GB	3 months ago
welcome@jaisairams-Laptop ~ % ollama run mistral:latest
>>> Send a message (/? for help)



# Request 

```
{
  "model": "mistral",
  "prompt": "[INST] why is the sky blue? [/INST]",
  "raw": true,
  "stream": false
}

```

# Response

```
{
    "model": "mistral",
    "created_at": "2024-08-17T16:00:51.4657Z",
    "response": " The color of the sky appears blue due to a process called Rayleigh scattering. As sunlight reaches Earth's atmosphere, it interacts with molecules and particles in the air, such as nitrogen and oxygen. These particles scatter the shorter wavelengths of light, particularly the blue light, more effectively than other colors. This scattered blue light is what we observe when looking up at the sky. However, during sunrise or sunset, the sky can appear red, pink, orange, or purple due to the scattering of longer wavelengths of light by larger particles in the atmosphere, such as dust and water droplets.",
    "done": true,
    "total_duration": 2501640875,
    "load_duration": 1778333,
    "prompt_eval_count": 10,
    "prompt_eval_duration": 246455000,
    "eval_count": 130,
    "eval_duration": 2250240000
}

```
