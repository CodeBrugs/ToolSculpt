**User Manual - ToolSculpt**

# Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Installation Steps](#installation-steps)
3. [Getting Started](#getting-started)
    - [Launching ToolSculpt](#launching-toolsculpt)
    - [AutoMagico: Your Learning Companion](#automagico-your-learning-companion)
    - [CodeSculptor: Crafting Code with Ease](#codesculptor-crafting-code-with-ease)
4. [Creating Your First Tool](#creating-your-first-tool)
    - [Using CodeSculptor Templates](#using-codesculptor-templates)
    - [Customizing Tool Assets](#customizing-tool-assets)
5. [Integrating with CodeBrugs Repositories](#integrating-with-codebrugs-repositories)
6. [User Interface Overview](#user-interface-overview)
    - [GUI Components](#gui-components)
    - [CLI Commands](#cli-commands)
7. [Troubleshooting](#troubleshooting)
8. [Feedback and Support](#feedback-and-support)
9. [Contributing to ToolSculpt](#contributing-to-toolsculpt)
10. [License](#license)

## Introduction

Welcome to *ToolSculpt*, your creative companion in the world of software development! This user manual will guide you through the installation, usage, and customization of *ToolSculpt*. Whether you're a seasoned developer or just getting started, *ToolSculpt* is designed to simplify your workflow and enhance your coding experience.

## Installation

### Prerequisites

Before installing *ToolSculpt*, ensure you have the following prerequisites:

- Python 3.x installed
- Virtual environment (optional but recommended)

### Installation Steps

1. Clone the *ToolSculpt* repository to your local machine:

```bash
git clone https://github.com/ToolSculpt/toolsculpt.git
```

2. Navigate to the project directory:

```bash
cd toolsculpt
```

3. (Optional) Set up a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Getting Started

### Launching ToolSculpt

Once installed, you can launch *ToolSculpt* using the following command:

```bash
python src/interface/CLI/command_line.py
```

This will open the command-line interface. Alternatively, you can explore the graphical interface by running:

```bash
python src/interface/GUI/main_window.py
```

### AutoMagico: Your Learning Companion

*AutoMagico* is the heart of *ToolSculpt*, continuously learning and evolving with each use. It suggests improvements to your code and adapts to your coding preferences over time.

### CodeSculptor: Crafting Code with Ease

*CodeSculptor* provides an intuitive interface for creatively crafting and generating code. Utilize predefined templates to expedite the creation of diverse tools.

## Creating Your First Tool

### Using CodeSculptor Templates

1. Launch *ToolSculpt* and navigate to *CodeSculptor*.
2. Choose a template from the available options.
3. Follow the prompts to customize the template according to your requirements.

### Customizing Tool Assets

1. For each tool, a folder named `assets/` is created.
2. Place images, videos, or any other assets in this folder to enhance the presentation of your tool.

## Integrating with CodeBrugs Repositories

*ToolSculpt* seamlessly integrates with your existing *CodeBrugs* repositories. Link your repositories to leverage accumulated knowledge and streamline the creation of new tools.

## User Interface Overview

### GUI Components

The graphical interface features various components for easy navigation and tool creation. Refer to the documentation for detailed information on each component.

### CLI Commands

The command-line interface provides commands for efficient tool creation and management. Refer to the CLI documentation for a list of available commands.

## Troubleshooting

Encountering issues? Check the troubleshooting section in the documentation for common problems and solutions.

## Feedback and Support

We value your feedback! If you have questions, encounter issues, or want to share your experience, visit our [developer forum](https://forums.toolsculpt.com) or contact our support team at [support@toolsculpt.com](mailto:support@toolsculpt.com).

## Contributing to ToolSculpt

Interested in contributing to *ToolSculpt*? Check the [developer guide](docs/developer_guide.md) for information on how to contribute, submit bug reports, and more.

## License

*ToolSculpt* is distributed under the [Creative Commons Attribution 4.0 International License](LICENSE). Please review the license before using or contributing to the project.

Enjoy exploring the creative possibilities with *ToolSculpt*! Happy coding!
