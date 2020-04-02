---
demoVideoId: uI1nMmEz5Mo
getStartedVideoId: DlLemGQa1B0
---

# Covfefe-19
Covfefe-19 is an API packaged into a browser extension which helps people validate the information they see online about COVID-19. It takes in statements about the coronavirus from users' browsers and returns relevant sources including how similar each source's information is to the statement - along with our own summary statistics (credibility, toxicity, etc.). In the browser extension, users can see all of this data to keep them informed in the face of so much misleading information.

{% include youtubePlayer.html id=page.demoVideoId %}

---
## Requirements
You need to have Node.js installed.
https://nodejs.org/en/

---
## Installation
{% include youtubePlayer.html id=page.getStartedVideoId %}

1. Download the browser extension.
{% raw %}
<button onclick="window.open('https://covid.arjungandhi.com/build.zip')">Download</button>
{% endraw %}

2. Go to chrome://extensions/

3. In the top right corner, make sure that Developer Mode is toggled on.

4. Click 'Load Unpacked' in the top right corner and select the build folder.

---
## Usage
1. Highlight any text that you want to fact-check with your cursor.

2. Click on the Covfefe-19 extension icon.

3. The extension will check the content against our API and show you the results.

---
## Team

| <a href="https://www.arjungandhi.com" target="_blank">**Arjun Gandhi**</a> | <a href="https://meghnadash.design" target="_blank">**Meghna Dash**</a> | <a href="https://github.com/sidharth-potdar" target="_blank">**Sidharth Potdar**</a> |
| :---: |:---:| :---:|
| [![Arjun Gandhi](https://avatars1.githubusercontent.com/u/33171158?v=3&s=200)](http://www.arjungandhi.com)    | [![Meghna Dash](https://avatars1.githubusercontent.com/u/44626500?v=3&s=200)](http://meghnadash.desigh) | [![Sidharth Potdar](https://avatars1.githubusercontent.com/u/32080078?v=3&s=200)](https://github.com/sidharth-potdar)  |
| Arjun worked on building the initial prototype and deployed it to AWS. | Meghna created a browser extension that enables users to query our API to verify information online. | Sidharth worked on the API and cloud architecture, and helped out with the browser extension as well.|
| <a href="https://www.arjungandhi.com" target="_blank">`Website`</a> | <a href="https://meghnadash.design" target="_blank">`Website`</a> | <a href="https://github.com/sidharth-potdar" target="_blank">`GitHub`</a> |


---

## Next for Covfefe-19
The next step would be to get our tool in as many hands as possible and get feedback. We want feedback on performance, usefulness, user experiences, everything. We specifically think we can improve some of the statistics and information we provide, but we definitely want to get as much data as possible.


---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
