const ChromeBrowser = require("./browserclass/browseroptions");

async function main() {
  const browser = new ChromeBrowser();

  // Read commands from the JSON file
  const filePath = "commands.json";
  await browser.executeCommandsFromFile(filePath);

  // ***************************************************************** //

  // Enter the URL of api(GET Method) to execute the Commands.
  // const apiUrl = "https://example.com/";
  // await browser.executeCommandsFromApi(apiUrl);

  // ***************************************************************** //

  // Open Respective link in chrome Browser
  //   await browser.open("https://www.example.com");

  // Save the current webpage to a file
  // await browser.savePage("./savedpages/page.html");

  // Click on the link with the specified link text
  //   await browser.clickOnLink("More information...");

  // Close the Currect Chrome Window
  //   await browser.close();
}

main();
