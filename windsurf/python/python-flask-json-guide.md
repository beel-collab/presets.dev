---
trigger: manual
title: "Python Flask JSON Guide"
description: "Developers working on automation and visualization in Factorio could use this prompt to create a Flask API that converts JSON data from FUE5 MOD to SVG using Drawscape Factorio."
tags: ["python"]
author:
  name: Community
  url: 'https://github.com/beel-collab/presets.dev'
---

This project is heavily reliant on our custom Drawscape Factorio python module.Here is code examples of how to use the module:```from drawscape_factorio import create as createFactoriofrom drawscape_factorio import importFUE5with open('/path/to/exported-entities.json, 'r') as file:json_data = json.load(file)data = importFUE5(json_data)result = createFactorio(data, {'theme_name': 'default','color_scheme': 'main','show_layers': ['assets', 'belts', 'walls', 'rails', 'electrical', 'spaceship']})with open(output_file_name, 'w') as f:f.write(result['svg_string'])````Here is my environment.yml that I'm running the project inname: drawscape_apichannels:
