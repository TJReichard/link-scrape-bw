# link-scrape-bw

Build a quick scraper for links of social media posts within a brandwatch query, as it seems to be impossible to get them without manual labour otherwise.

# Necessary python libraries
- python-dotenv
- selenium
  - build for use with geckodriver in its current version

# Limitations

- You will need your own brandwatch account and create your own queries.
- The code is made for one specific query in a very specific project, however it uses brandwatch html identifiers. It will break if the platform owner decides to change class names/attributes within query output
- The script has issues with the cookie banner if the settings are not saved manually before starting the script and will error out as it is not handled 
- You will most likely need to change/add additional identifiers and change the csv creation logic if you are looking to achieve something else.
- For the current need, it was enough to map the entry number and the link for each post.


Feel free to use and adapt the code for your own usecases.
