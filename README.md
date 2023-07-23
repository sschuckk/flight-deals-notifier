<!-- Template get from: https://github.com/othneildrew/Best-README-Template -->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Flight Deal Notifier Script</h3>

  <p align="center">
    <br />
    <a href="https://github.com/sschuckk/flight-deals-notifier/issues">Report Bug</a>
    ·
    <a href="https://github.com/sschuckk/flight-deals-notifier/issues">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
Are you weary of visiting multiple websites daily just to see if there are any enticing flight deals available?

This script uses APIs to search for flight deals from a list of cities and notifies the user via SMS if a deal
is found with a price lower than the specified amount.

With this, you can define a date range, specify the cities you want to visit, and let the script work for you.

**Note:** Before running this script, ensure that the necessary credentials and environment variables are properly
configured for accessing the Google Sheets, Sheety, Tequila and Twilio API.

[![Product presentation][product-banner]](https://github.com/sschuckk/selenium-webtest-booking)

### Built With

[![Python][Python.com]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started


### Prerequisites
To use the Script:
* Python: https://www.python.org/downloads/
* Pip: https://pip.pypa.io/en/stable/installation/
* Git: https://git-scm.com/downloads

To use the APIs:
* Create a free account on Sheety: https://sheety.co/
* Create a free account on Tequila: https://tequila-api.kiwi.com
* Create a free account on Twilio: https://www.twilio.com/

### Installation

1. Clone the repo.
   ```sh
   git clone https://github.com/sschuckk/flight-deals-notifier.git
   ```
2. Install the packages according to the configuration file requirements.txt.
   ```sh
   pip install -r requirements.txt
   ```
3. Download the flight deals sheet file and upload it to your Google Docs. 
   https://github.com/sschuckk/flight-deals-notifier/blob/main/Flight%20Deals.xlsx


4. Use your API credentials in these variables:
    ```sh
   data_manager.py
          SHEETY_ENDPOINT
   flight_search.py
          TEQUILA_ENDPOINT
          TEQUILA_API_KEY
   notifier_manager.py
          TWILIO_SID
          TWILIO_AUTH_TOKEN
          TWILIO_VIRTUAL_NUMBER
          TWILIO_VERIFIED_NUMBER
   ```
   <p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

The project can be run by a terminal or directly in your favorite IDE.
You can configure a task scheduler on Windows/Linux to run the script daily to get the best offers.
I recommend to use https://www.pythonanywhere.com/ to execute the script remotely.

1. Configure the Google Sheets:
   [![Product presentation][product-exec3]]()
    - Define the date range for flight searches. Use just one start/end date for all search.
    - Define the City Origen. One city per row, multiple cities per column. 
      - All City Origen will be used against all City destination.
    - Define the City Destination. One city per row, multiple cities per column.
    - Don't worry if you don't know each Code. The script will find it for you.
    - Define the Lowest price for each City Destination.
      - If a flight is found with a price lower than the specified lowest price the SMS will be sent.
   
    **Note:** The spreadsheet **doc** contains the description of each column.


2. For a simples execution:
   ```sh
   python main.py
   ```

## Output:

_Logs printed-out on terminal:_
[![Product presentation][product-exec1]]()

_SMS received on smartphone:_
[![Product presentation][product-exec2]]()

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [ ] Send Whatsapp messages
- [ ] Send Email messages
- [ ] Create a link direct to the deals

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some new feature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the [MIT](https://opensource.org/license/mit/) License. It’s free, no legal restrictions, why not try it out?

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT 
## Contact

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-banner]: images/banner.png
[product-exec1]: images/log_messages.png
[product-exec2]: images/sms_messages.jpg
[product-exec3]: images/data_entry.png
[Python.com]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/ 
[Selenium.com]: https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white
[Selenium-url]: https://www.selenium.dev/
[Pytest.com]: https://img.shields.io/badge/PYTEST-007ACC?style=for-the-badge&logo=pytest&logoColor=orange
[Pytest-url]: https://docs.pytest.org/