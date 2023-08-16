const axios = require('axios'); // Use axios instead of node-fetch
const { Octokit } = require('@octokit/rest');

async function main() {
  const token = process.env.PERSONAL_ACCESS_TOKEN;
  console.log('Token:', token);

  const eventData = JSON.parse(process.env.GITHUB_EVENT);
  const issueNumber = eventData.issue.number;
  console.log('Issue Number:', issueNumber);

  const octokit = new Octokit({
    auth: `token ${token}`,
    request: {
      fetch: axios
    }
  });

  try {
    // Rest of your script
  } catch (error) {
    // Rest of your script
  }
}

main();
