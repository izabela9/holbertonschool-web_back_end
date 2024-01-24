function getResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (success) {
        resolve({ status: 200, body: 'Success' });
      } else {
        reject(new Error('The fake API is not working currently'));
      }
    }, 10);
	  .catch((error) => {
      console.error('Error in getResponseFromAPI:', error.message);
  });
});
}
export default getResponseFromAPI;
