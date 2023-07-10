# Creating a Turbox Package for Your Application

## Step 1: Download the AppBuilder.py File

- Go to the [AppBuilder.py file](https://github.com/pandap17/turbox-packages/tree/main/appbuilder) in the Turbox Packages GitHub repository.
- Download the `AppBuilder.py` file to your local machine.

## Step 2: Run the AppBuilder.py File

- Open a terminal or command prompt on your computer.
- Navigate to the directory where you downloaded the `AppBuilder.py` file.
- Run the file using the appropriate command for your operating system (e.g., `python AppBuilder.py`).
- After running the file, a dialog window will appear.

## Step 3: Select Your Sprite Files

- In the dialog window, you will be prompted to select sprite files (files with a `.sprite3` extension).
- Choose all the sprite files that are part of your application.
- Make sure to select all the relevant files to ensure your application works correctly.

## Step 4: Include Extensions (if applicable)

- After selecting the sprite files, another dialog window will appear.
- This dialog will ask you to paste the links to your extensions (one link per line).
- If your application uses any JavaScript (JS) extensions, paste the links into the dialog window.
- If you don't have any extensions to include, leave the dialog box empty.
- Click the "Save" button to continue.

## Step 5: Save Your Turbox Package

- Once you have selected the sprite files and entered the extension links (if applicable), the JSON output will be generated.
- A file dialog window will appear, asking you to choose the directory and enter a filename for your Turbox Package.
- Select the directory where you want to save your package and enter a filename with a `.tpkg` extension (e.g., `myapp.tpkg`).
- Click the "Save" button to save your Turbox Package.

## Step 6: Submit a Pull Request

- Fork the [turbox-packages](https://github.com/pandap17/turbox-packages) repository on GitHub.
- Ensure that your forked repository is up to date with the latest changes from the main repository.
- Add your Turbox Package file (`myapp.tpkg`) to the main directory of your forked repository.
- Commit and push the changes to your forked repository.
- Submit a pull request to the main `turbox-packages` repository to have your package reviewed and potentially added.

By following these steps, you can create a Turbox Package for your application. The package will contain the selected sprite files and optional extensions, and it will be exported as a `.tpkg` file to the directory of your choice. Finally, you can submit a pull request to contribute your package to the main Turbox Packages repository.
