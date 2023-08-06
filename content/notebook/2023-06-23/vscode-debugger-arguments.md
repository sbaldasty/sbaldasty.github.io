---
title: Passing command line arguments to python program in Debug mode
topics: []
---

To pass command line arguments to a python program started with Debug in VSCode, [create](https://code.visualstudio.com/docs/python/debugging) a launch.json file, [configure](https://stackoverflow.com/questions/66971452/how-to-add-virtual-environment-to-vscode-launch-json) the virtual environment, and [add](https://stackoverflow.com/questions/57889703/in-visual-studio-code-how-to-pass-arguments-in-launch-json) args to it. For me it only works using _Run > Start Debugging_, rather than the _Debug_ button.