selenate
========

Web Automation made easy, built around Selenium

## Setting up
1. First off make sure your browser is up to date
[![Download: Fast, Fun, Awesome](https://affiliates.mozilla.org/media/uploads/banners/910443de740d4343fa874c37fc536bd89998c937.png?from_affiliates)](//affiliates.mozilla.org/link/banner/54231)

2. Download the latest selenium server and 
[save it as selenium-server.jar](http://selenium-release.storage.googleapis.com/index.html)

3. Install selenate
```bash
pip install selenate
```

## Coding
Here's some basic code to start a browser and navigate a little bit
```python
from selenate import Selenate
browser = Selenate()
browser.get("https://github.com/wmak/selenate")
browser.click(".mega-octicon")
```
