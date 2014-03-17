selenate
========
[![Latest Version](https://pypip.in/v/selenate/badge.png)](https://pypi.python.org/pypi/selenate/)
[![Downloads](https://pypip.in/d/selenate/badge.png)](https://pypi.python.org/pypi/selenate/)

Web Automation made easy, built around Selenium

## Setting up
1. First off make sure your browser is up to date
[![Download: Fast, Fun, Awesome](https://affiliates.mozilla.org/media/uploads/banners/910443de740d4343fa874c37fc536bd89998c937.png?from_affiliates)](//affiliates.mozilla.org/link/banner/54231)

2. Download the latest selenium server(selenium-server-standalone-x.xx.x.jar) and 
[save it as selenium-server.jar](http://selenium-release.storage.googleapis.com/index.html). This file should go wherever your application will run out of.

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
