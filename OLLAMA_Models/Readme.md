# LLAMA3
```
welcome@jaisairams-Laptop ~ % ollama list
NAME          	ID          	SIZE  	MODIFIED
llama2:13b    	d475bf4c50bc	7.4 GB	13 days ago
llama2:latest 	78e26419b446	3.8 GB	13 days ago
llama3:latest 	365c0bd3c000	4.7 GB	2 months ago
mistral:latest	61e88e884507	4.1 GB	3 months ago
welcome@jaisairams-Laptop ~ % ollama run llama3:latest
>>> Send a message (/? for help)

```
# LLAMA Request 

```
{
    "model": "llama3",
    "prompt": "Why is the sky blue?",
     "stream": false
     
}
```

# LLAMA Response
```
{"model":"llama3","created_at":"2024-08-17T15:23:25.033486Z","response":"What a great question!\n\nThe short answer is that the sky appears blue because of a phenomenon called scattering. Here's what happens:\n\n1. **Sunlight**: When the sun emits light, it contains all the colors of the visible spectrum (red, orange, yellow, green, blue, indigo, and violet).\n2. **Atmosphere**: As sunlight travels through the Earth's atmosphere, it encounters tiny molecules of gases like nitrogen (N2) and oxygen (O2). These molecules are much smaller than the wavelength of light.\n3. **Scattering**: When a photon of light (a particle of light) hits one of these small molecules, it scatters in all directions. This is because the molecule's size is comparable to the wavelength of light, allowing for efficient scattering.\n\nNow, here's the important part:\n\n* **Blue light has a shorter wavelength** than other colors. It's like a tiny photon with more energy.\n* **Scattering favors shorter wavelengths**: Since blue light has a shorter wavelength, it scatters more efficiently than longer-wavelength lights like red or orange.\n* **More scattering means more blue**: As sunlight travels through the atmosphere, it encounters many small molecules that scatter the blue light in all directions. This scattered blue light reaches our eyes from all parts of the sky.\n\nSo, when we look at the sky, we see the combined effect of all this scattered blue light, which appears as a bright blue color. Voilà! The sky is blue!\n\n(Note: This explanation assumes a clear atmosphere with no major aerosols or pollution. In cases where there are aerosols or pollution particles in the air, the scattering can be affected, and the sky may appear more hazy or take on different colors.)","done":true,"context":[128006,882,128007,271,10445,374,279,13180,6437,30,128009,128006,78191,128007,271,3923,264,2294,3488,2268,791,2875,4320,374,430,279,13180,8111,6437,1606,315,264,25885,2663,72916,13,5810,596,1148,8741,1473,16,13,3146,31192,4238,96618,3277,279,7160,73880,3177,11,433,5727,682,279,8146,315,279,9621,20326,320,1171,11,19087,11,14071,11,6307,11,6437,11,1280,7992,11,323,80836,4390,17,13,3146,1688,8801,8182,96618,1666,40120,35292,1555,279,9420,596,16975,11,433,35006,13987,35715,315,45612,1093,47503,320,45,17,8,323,24463,320,46,17,570,4314,35715,527,1790,9333,1109,279,46406,315,3177,627,18,13,3146,3407,31436,96618,3277,264,69010,315,3177,320,64,19320,315,3177,8,13280,832,315,1521,2678,35715,11,433,1156,10385,304,682,18445,13,1115,374,1606,279,43030,596,1404,374,30139,311,279,46406,315,3177,11,10923,369,11297,72916,382,7184,11,1618,596,279,3062,961,1473,9,3146,10544,3177,706,264,24210,46406,334,1109,1023,8146,13,1102,596,1093,264,13987,69010,449,810,4907,627,9,3146,3407,31436,54947,24210,93959,96618,8876,6437,3177,706,264,24210,46406,11,433,1156,10385,810,30820,1109,5129,2695,35961,13001,1093,2579,477,19087,627,9,3146,7816,72916,3445,810,6437,96618,1666,40120,35292,1555,279,16975,11,433,35006,1690,2678,35715,430,45577,279,6437,3177,304,682,18445,13,1115,38067,6437,3177,25501,1057,6548,505,682,5596,315,279,13180,382,4516,11,994,584,1427,520,279,13180,11,584,1518,279,11093,2515,315,682,420,38067,6437,3177,11,902,8111,439,264,10107,6437,1933,13,29179,321,6496,0,578,13180,374,6437,2268,90489,25,1115,16540,22204,264,2867,16975,449,912,3682,49825,3145,477,25793,13,763,5157,1405,1070,527,49825,3145,477,25793,19252,304,279,3805,11,279,72916,649,387,11754,11,323,279,13180,1253,5101,810,305,13933,477,1935,389,2204,8146,6266,128009],"total_duration":7140020584,"load_duration":4322292,"prompt_eval_duration":249684000,"eval_count":354,"eval_duration":6883889000}
```

# Mistral Model Running

```
Use "ollama [command] --help" for more information about a command.
welcome@jaisairams-Laptop ~ % ollama list
NAME          	ID          	SIZE  	MODIFIED
llama2:13b    	d475bf4c50bc	7.4 GB	13 days ago
llama2:latest 	78e26419b446	3.8 GB	13 days ago
llama3:latest 	365c0bd3c000	4.7 GB	2 months ago
mistral:latest	61e88e884507	4.1 GB	3 months ago
welcome@jaisairams-Laptop ~ % ollama run mistral:latest
>>> Send a message (/? for help)

```


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
