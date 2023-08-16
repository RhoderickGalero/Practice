const axios = require('axios');

// Replace 'YOUR_PAT_HERE' with your actual PAT
const token = 'PERSONAL_ACCESS_TOKEN';
const apiUrl = 'https://api.github.com';

// Example: Get the authenticated user's profile
axios.get(`${apiUrl}/user`, {
  headers: {
    Authorization: `Bearer ${token}`
  }
})
.then(response => {
  console.log('Authenticated User:', response.data);
})
.catch(error => {
  console.error('Error:', error);
});
