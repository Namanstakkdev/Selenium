const { Builder, By, Capabilities } = require("selenium-webdriver");
const chrome = require("selenium-webdriver/chrome");
const fs = require("fs");
const axios = require("axios");

class ChromeBrowser {
  constructor() {
    const chromeOptions = new chrome.Options();
    chromeOptions.addArguments("--start-maximized");

    this.driver = new Builder()
      .forBrowser("chrome")
      .setChromeOptions(chromeOptions)
      .setChromeService(
        new chrome.ServiceBuilder("./browserclass/chromedriver.exe")
      )
      .build();
  }

  async open(url) {
    try {
      await this.driver.get(url);
    } catch (error) {
      console.error("Error opening URL:", error);
      await browser.takeErrorSnapshot(error);
    }
  }

  async close() {
    try {
      await this.driver.quit();
    } catch (error) {
      console.error("Error closing browser:", error);
      await browser.takeErrorSnapshot(error);
    }
  }

  async savePage(filePath) {
    try {
      const pageSource = await this.driver.getPageSource();
      fs.writeFileSync(filePath, pageSource, "utf8");
      console.log("Page saved successfully!");
    } catch (error) {
      console.error("Error saving page:", error);
      await browser.takeErrorSnapshot(error);
    }
  }

  async clickOnLink(linkText) {
    try {
      const linkElement = await this.driver.findElement(By.linkText(linkText));
      await linkElement.click();
      console.log("Clicked on the link successfully!");
    } catch (error) {
      console.error("Error clicking on the link:", error);
      await browser.takeErrorSnapshot(error);
    }
  }

  async typeText(selector, text) {
    try {
      const element = await this.driver.findElement(By.css(selector));
      await element.sendKeys(text);
    } catch (error) {
      console.error("Error typing text:", error);
      await browser.takeErrorSnapshot(error);
    }
  }

  async takeErrorSnapshot(error) {
    try {
      // Create an "errors" folder if it doesn't exist
      const errorsFolder = "./errors";
      if (!fs.existsSync(errorsFolder)) {
        fs.mkdirSync(errorsFolder);
      }

      // Take a screenshot
      const timestamp = new Date().toISOString().replace(/:/g, "-");
      const screenshotPath = `${errorsFolder}/error_${timestamp}.png`;
      await this.driver.takeScreenshot().then((data) => {
        fs.writeFileSync(screenshotPath, data, "base64");
        console.log(`Error snapshot saved: ${screenshotPath}`);
      });
    } catch (snapshotError) {
      console.error("Error taking snapshot:", snapshotError);
    }

    // Rethrow the original error
    throw error;
  }

  async executeCommand(command) {
    const { action, args } = command;
    switch (action) {
      case "open":
        await this.open(args.url);
        break;
      case "close":
        await this.close();
        break;
      case "savePage":
        await this.savePage(args.filePath);
        break;
      case "typeText":
        await this.typeText(args.selector, args.text);
        break;
      case "clickOnLink":
        await this.clickOnLink(args.linkText);
        break;
      default:
        console.error("Invalid command:", command);
        await browser.takeErrorSnapshot(error);
    }
  }

  async executeCommandsFromFile(filePath) {
    try {
      const commands = JSON.parse(fs.readFileSync(filePath, "utf8"));
      for (const command of commands) {
        await this.executeCommand(command);
      }
    } catch (error) {
      console.error("Error executing commands from file:", error);
      await browser.takeErrorSnapshot(error);
    }
  }

  async executeCommandsFromApi(apiUrl) {
    try {
      const response = await axios.get(apiUrl);
      const commands = response.data;

      for (const command of commands) {
        await this.executeCommand(command);
      }
    } catch (error) {
      console.error("Error executing commands from API:", error);
      await this.takeErrorSnapshot(error);
    }
  }
}

module.exports = ChromeBrowser;
