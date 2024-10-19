const cityInput = document.querySelector('.city-input'); // Selects the input element for the city name
const searchBtn = document.querySelector('.search-btn'); // Selects the search button element
const geolocationBtn = document.querySelector('.geolocation-btn'); // Selects the geolocation button element
const starBtn = document.querySelector('.star-btn'); // Selects the star button element

const weatherInfoSection = document.querySelector('.weather-info'); // Selects the section displaying weather information
const notFoundSection = document.querySelector('.not-found'); // Selects the section displayed when city is not found
const searchCitySection = document.querySelector('.search-city'); // Selects the section for searching a city

const countryTxt = document.querySelector('.country-txt'); // Selects the element displaying the country name
const tempTxt = document.querySelector('.temp-txt'); // Selects the element displaying the temperature
const conditionTxt = document.querySelector('.condition-txt'); // Selects the element displaying the weather condition
const humidityValueTxt = document.querySelector('.humidity-value-txt'); // Selects the element displaying the humidity value
const windValueTxt = document.querySelector('.wind-speed-value-txt'); // Selects the element displaying the wind speed value
const weatherSummaryImg = document.querySelector('.weather-summary-img'); // Selects the image element for weather summary
const currentDateTxt = document.querySelector('.current-date-txt'); // Selects the element displaying the current date

const forecastItemsContainer = document.querySelector('.forecast-items-container'); // Selects the container for forecast items

const apiKey = '4e5f3c11708804dcc5b155197bf79891'; // API key for accessing the weather service

searchBtn.addEventListener('click', () => { // Adds a click event listener to the search button
    if (cityInput.value.trim() != '') { // Checks if the city input is not empty
        updateWeatherInfo(cityInput.value); // Calls the function to update weather info with the city name
        cityInput.value = ''; // Clears the city input field
        cityInput.blur(); // Removes focus from the city input field
    }
});

cityInput.addEventListener('keydown', (event) => { // Adds a keydown event listener to the city input field
    if (event.key == 'Enter' && cityInput.value.trim() != '') { // Checks if the Enter key is pressed and the input is not empty
        updateWeatherInfo(cityInput.value); // Calls the function to update weather info with the city name
        cityInput.value = ''; // Clears the city input field
        cityInput.blur(); // Removes focus from the city input field
    }
});

geolocationBtn.addEventListener('click', () => { // Adds a click event listener to the geolocation button
    if (navigator.geolocation) { // Checks if geolocation is supported by the browser
        console.log("Geolocation supported"); // Logs that geolocation is supported
        navigator.geolocation.getCurrentPosition(getWeatherByLocation, showError); // Gets the current position and calls the function to get weather by location
    } else {
        alert("Geolocation is not supported by this browser."); // Alerts the user if geolocation is not supported
    }
});

async function getFetchData(endPoint, query) { // Defines an async function to fetch data from the API
    try {
        const apiURL = `https://api.openweathermap.org/data/2.5/${endPoint}?${query}&appid=${apiKey}&units=metric`; // Constructs the API URL
        const response = await fetch(apiURL); // Fetches data from the API

        if (!response.ok) { // Checks if the response is not OK
            console.error(`Error: ${response.statusText}`); // Logs the error status text
            throw new Error(`API request failed: ${response.status}`); // Throws an error with the status code
        }

        return response.json(); // Returns the response data as JSON
    } catch (error) {
        console.error('Failed to fetch data:', error); // Logs the error if fetching data fails
        throw error; // Throws the error
    }
}

function getWeatherIcon(id) { // Defines a function to get the weather icon based on weather ID
    if (id <= 232) return 'thunderstorm.svg'; // Returns thunderstorm icon for IDs <= 232
    if (id <= 321) return 'drizzle.svg'; // Returns drizzle icon for IDs <= 321
    if (id <= 531) return 'rain.svg'; // Returns rain icon for IDs <= 531
    if (id <= 622) return 'snow.svg'; // Returns snow icon for IDs <= 622
    if (id <= 781) return 'atmosphere.svg'; // Returns atmosphere icon for IDs <= 781
    if (id === 800) return 'clear.svg'; // Returns clear icon for ID 800
    return 'clouds.svg'; // Returns clouds icon for other IDs
}

function getCurrentDate() { // Defines a function to get the current date in a specific format
    const currentDate = new Date(); // Gets the current date
    const options = { // Defines options for date formatting
        weekday: 'short', // Short weekday format
        day: '2-digit', // 2-digit day format
        month: 'short' // Short month format
    };

    return currentDate.toLocaleDateString('en-GB', options); // Returns the formatted date string
}

function updateBackgroundImage(icon) { // Defines a function to update the background image based on the weather icon
    const body = document.body;
    switch (icon) {
        case 'thunderstorm.svg':
            body.style.backgroundImage = 'url("assets/background/thunderstorm.jpg")';
            break;
        case 'drizzle.svg':
            body.style.backgroundImage = 'url("assets/background/drizzle.jpg")';
            break;
        case 'rain.svg':
            body.style.backgroundImage = 'url("assets/background/rain.jpg")';
            break;
        case 'snow.svg':
            body.style.backgroundImage = 'url("assets/background/snow.jpg")';
            break;
        case 'atmosphere.svg':
            body.style.backgroundImage = 'url("assets/background/atmosphere.jpg")';
            break;
        case 'clear.svg':
            body.style.backgroundImage = 'url("assets/background/clear.jpg")';
            break;
        case 'clouds.svg':
            body.style.backgroundImage = 'url("assets/background/clouds.jpg")';
            break;
        default:
            body.style.backgroundImage = 'url("assets/background/bg.jpg")';
            break;
    }
}

async function updateWeatherInfo(city) { // Defines an async function to update weather information for a city
    try {
        const weatherData = await getFetchData('weather', `q=${city}`); // Fetches weather data for the city
        if (weatherData.cod != 200) { // Checks if the response code is not 200 (OK)
            showDisplaySection(notFoundSection); // Shows the not found section
            return; // Exits the function
        }

        const { // Destructures the weather data
            name: country, // Gets the country name
            main: { temp, humidity }, // Gets the temperature and humidity
            weather: [{ id, main }], // Gets the weather ID and main condition
            wind: { speed } // Gets the wind speed
        } = weatherData;

        countryTxt.textContent = country; // Updates the country text content
        tempTxt.textContent = Math.round(temp) + ' °C'; // Updates the temperature text content
        conditionTxt.textContent = main; // Updates the condition text content
        humidityValueTxt.textContent = humidity + '%'; // Updates the humidity value text content
        windValueTxt.textContent = speed + ' M/s'; // Updates the wind speed value text content

        currentDateTxt.textContent = getCurrentDate(); // Updates the current date text content
        const weatherIcon = getWeatherIcon(id); // Get the weather icon based on weather ID
        weatherSummaryImg.src = `assets/weather/${weatherIcon}`; // Updates the weather summary image source

        // Update background image
        updateBackgroundImage(weatherIcon); // Update the background image based on the weather icon

        await updateForecastsInfo(city); // Calls the function to update forecast information
        showDisplaySection(weatherInfoSection); // Shows the weather information section
    } catch (error) {
        console.error("Failed to fetch data", error); // Logs the error if fetching data fails
        showDisplaySection(notFoundSection); // Shows the not found section
    }
}

async function updateForecastsInfo(city) { // Defines an async function to update forecast information for a city
    try {
        const forecastsData = await getFetchData('forecast/daily', `q=${city}&cnt=7`); // Fetches 7-day forecast data for the city
        forecastItemsContainer.innerHTML = ''; // Clears the forecast items container

        forecastsData.list.forEach(forecastWeather => { // Iterates over the forecast data list
            updateForecastItems(forecastWeather); // Calls the function to update forecast items
        });
    } catch (error) {
        console.error("Failed to fetch data:", error); // Logs the error if fetching data fails
    }
}

function updateForecastItems(weatherData) { // Defines a function to update forecast items
    const { // Destructures the weather data
        dt: timestamp, // Gets the timestamp
        weather: [{ id }], // Gets the weather ID
        temp: { day: temp } // Gets the day temperature
    } = weatherData;

    const date = new Date(timestamp * 1000); // Converts UNIX timestamp to readable date
    const dateOptions = { // Defines options for date formatting
        day: '2-digit', // 2-digit day format
        month: 'short' // Short month format
    };
    const dateResult = date.toLocaleDateString('en-US', dateOptions); // Formats the date string

    const forecastItem = ` // Defines the HTML structure for a forecast item
        <div class="forecast-item">
            <h5 class="forecast-item-date regular-txt">${dateResult}</h5> // Displays the forecast date
            <img src="assets/weather/${getWeatherIcon(id)}" class="forecast-item-img"> // Displays the forecast weather icon
            <h5 class="forecast-item-temp">${Math.round(temp)} °C</h5> // Displays the forecast temperature
        </div>
    `;
    forecastItemsContainer.insertAdjacentHTML('beforeend', forecastItem); // Inserts the forecast item into the container
}

function showDisplaySection(section) { // Defines a function to show a specific display section
    [weatherInfoSection, searchCitySection, notFoundSection].forEach(sec => sec.style.display = 'none'); // Hides all sections
    section.style.display = 'flex'; // Shows the specified section
    if (section === notFoundSection || !document.body.style.backgroundImage) {
        document.body.style.backgroundImage = 'url("assets/background/bg.jpg")'; // Resets the background image to default
    }
}

function getWeatherByLocation(position) { // Defines a function to get weather by location
    const latitude = position.coords.latitude; // Gets the latitude from the position
    const longitude = position.coords.longitude; // Gets the longitude from the position
    console.log(`Latitude: ${latitude}, Longitude: ${longitude}`); // Logs the latitude and longitude
    fetchWeatherData(latitude, longitude); // Calls the function to fetch weather data by coordinates
}

function showError(error) { // Defines a function to handle geolocation errors
    console.error('Geolocation error:', error); // Logs the geolocation error
}

function fetchWeatherData(lat, lon) { // Defines a function to fetch weather data by coordinates
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=metric&appid=${apiKey}`; // Constructs the API URL

    fetch(apiUrl) // Fetches data from the API
        .then(response => response.json()) // Parses the response as JSON
        .then(data => { // Handles the response data
            document.querySelector('.country-txt').textContent = data.name; // Updates the country text content
            document.querySelector('.temp-txt').textContent = `${Math.round(data.main.temp)} °C`; // Updates the temperature text content
            document.querySelector('.condition-txt').textContent = data.weather[0].description; // Updates the condition text content
            document.querySelector('.humidity-value-txt').textContent = `${data.main.humidity}%`; // Updates the humidity value text content
            document.querySelector('.wind-speed-value-txt').textContent = `${data.wind.speed} M/s`; // Updates the wind speed value text content

            // Update current date
            currentDateTxt.textContent = getCurrentDate(); // Updates the current date text content

            // Update weather summary image
            const weatherIcon = getWeatherIcon(data.weather[0].id); // Get the weather icon based on weather ID
            document.querySelector('.weather-summary-img').src = `assets/weather/${weatherIcon}`; // Update the weather summary image source

            // Update background image
            updateBackgroundImage(weatherIcon); // Update the background image based on the weather icon

            // Hide the section-message and show the weather info
            showDisplaySection(weatherInfoSection); // Shows the weather information section

            // Fetch and display the 7-day forecast
            updateForecastsInfoByCoords(lat, lon); // Calls the function to update forecast information by coordinates
        })
        .catch(error => { // Handles errors in fetching data
            console.error('Error fetching weather data:', error); // Logs the error
            showDisplaySection(notFoundSection); // Shows the not found section
        });
}

async function updateForecastsInfoByCoords(lat, lon) { // Defines an async function to update forecast information by coordinates
    try {
        const forecastsData = await getFetchData('forecast/daily', `lat=${lat}&lon=${lon}&cnt=7`); // Fetches 7-day forecast data by coordinates
        forecastItemsContainer.innerHTML = ''; // Clears the forecast items container

        forecastsData.list.forEach(forecastWeather => { // Iterates over the forecast data list
            updateForecastItems(forecastWeather); // Calls the function to update forecast items
        });
    } catch (error) {
        console.error("Failed to fetch data:", error); // Logs the error if fetching data fails
    }
}

const weatherApiKey = '4e5f3c11708804dcc5b155197bf79891'; // API key for accessing the weather service
const autocompleteApiKey = '6CUP8tU+9GkFrECIwYOR0g==nD2yvJ8w33qefr82'; // API key for accessing the autocomplete service
const autocompleteApiURL = 'https://api.api-ninjas.com/v1/city?name=';

searchBtn.addEventListener('click', () => { // Adds a click event listener to the search button
    if (cityInput.value.trim() != '') { // Checks if the city input is not empty
        updateWeatherInfo(cityInput.value); // Calls the function to update weather info with the city name
        cityInput.value = ''; // Clears the city input field
        cityInput.blur(); // Removes focus from the city input field
    }
});

cityInput.addEventListener('keydown', (event) => { // Adds a keydown event listener to the city input field
    if (event.key == 'Enter' && cityInput.value.trim() != '') { // Checks if the Enter key is pressed and the input is not empty
        updateWeatherInfo(cityInput.value); // Calls the function to update weather info with the city name
        cityInput.value = ''; // Clears the city input field
        cityInput.blur(); // Removes focus from the city input field
    }
});

function autocomplete(inputElement) {
    let currentFocus;

    inputElement.addEventListener('input', function() {
        const query = this.value;
        closeAllLists();

        if (!query) return;

        fetch(autocompleteApiURL + query, {
            headers: {
                'X-Api-Key': autocompleteApiKey
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.length === 0) return;

            const autocompleteList = document.createElement('div');
            autocompleteList.setAttribute('id', inputElement.id + 'autocomplete-list');
            autocompleteList.setAttribute('class', 'autocomplete-items');
            inputElement.parentNode.appendChild(autocompleteList);

            data.forEach(cityData => {
                const cityName = `${cityData.name}, ${cityData.country}`;
                const item = document.createElement('div');
                item.innerHTML = `<strong>${cityName.substr(0, query.length)}</strong>${cityName.substr(query.length)}`;
                item.innerHTML += `<input type='hidden' value='${cityName}'>`;
                item.addEventListener('click', function() {
                    inputElement.value = this.getElementsByTagName('input')[0].value;
                    closeAllLists();
                });
                autocompleteList.appendChild(item);
            });
        })
        .catch(error => console.error('Error fetching city data:', error));
    });

    inputElement.addEventListener('keydown', function(e) {
        let items = document.getElementById(this.id + 'autocomplete-list');
        if (items) items = items.getElementsByTagName('div');

        if (e.keyCode === 40) {  // down arrow
            currentFocus++;
            addActive(items);
        } else if (e.keyCode === 38) {  // up arrow
            currentFocus--;
            addActive(items);
        } else if (e.keyCode === 13) {  // enter
            e.preventDefault();
            if (currentFocus > -1) {
                if (items) items[currentFocus].click();
            }
        }
    });

    function addActive(items) {
        if (!items) return false;
        removeActive(items);
        if (currentFocus >= items.length) currentFocus = 0;
        if (currentFocus < 0) currentFocus = items.length - 1;
        items[currentFocus].classList.add('autocomplete-active');
    }

    function removeActive(items) {
        for (let i = 0; i < items.length; i++) {
            items[i].classList.remove('autocomplete-active');
        }
    }

    function closeAllLists(elmnt) {
        const items = document.getElementsByClassName('autocomplete-items');
        for (let i = 0; i < items.length; i++) {
            if (elmnt !== items[i] && elmnt !== inputElement) {
                items[i].parentNode.removeChild(items[i]);
            }
        }
    }

    document.addEventListener('click', function(e) {
        closeAllLists(e.target);
    });
}

// Initialize the autocomplete function
autocomplete(document.getElementById('cityInput'));