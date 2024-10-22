const cityInput = document.querySelector('.city-input');
const searchBtn = document.querySelector('.search-btn');
const geolocationBtn = document.querySelector('.geolocation-btn');
const starBtn = document.querySelector('.star-btn');

const weatherInfoSection = document.querySelector('.weather-info');
const notFoundSection = document.querySelector('.not-found');
const searchCitySection = document.querySelector('.search-city');

const countryTxt = document.querySelector('.country-txt');
const tempTxt = document.querySelector('.temp-txt');
const conditionTxt = document.querySelector('.condition-txt');
const humidityValueTxt = document.querySelector('.humidity-value-txt');
const windValueTxt = document.querySelector('.wind-speed-value-txt');
const weatherSummaryImg = document.querySelector('.weather-summary-img');
const currentDateTxt = document.querySelector('.current-date-txt');

const forecastItemsContainer = document.querySelector('.forecast-items-container');

const apiKey = '4e5f3c11708804dcc5b155197bf79891';

searchBtn.addEventListener('click', () => {
    if (cityInput.value.trim() != '') {
        updateWeatherInfo(cityInput.value);
        cityInput.value = '';
        cityInput.blur();
    }
});

cityInput.addEventListener('keydown', (event) => {
    if (event.key == 'Enter' && cityInput.value.trim() != '') {
        updateWeatherInfo(cityInput.value);
        cityInput.value = '';
        cityInput.blur();
    }
});
geolocationBtn.addEventListener('click', () => {
    if (navigator.geolocation) {
        console.log("Geolocation supported");
        navigator.geolocation.getCurrentPosition(getWeatherByLocation, showError);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
});

let savedCities = [];

function updateSaveButtonIcon() {
    const cityName = countryTxt.textContent.trim();
    const saveBtn = document.querySelector('.save-btn');

    if (savedCities.includes(cityName)) {
        saveBtn.innerHTML = '<span class="material-symbols-outlined">bookmark_added</span>';
    } else {
        saveBtn.innerHTML = '<span class="material-symbols-outlined">bookmark_add</span>';
    }
}

document.querySelector('.save-btn').addEventListener('click', function () {
    const cityName = countryTxt.textContent.trim();
    const saveBtn = document.querySelector('.save-btn');

    if (cityName) {
        if (!savedCities.includes(cityName)) {
            savedCities.push(cityName);
            alert(`${cityName} has been saved!`);
        } else {
            savedCities = savedCities.filter(city => city !== cityName);
            alert(`${cityName} has been removed!`);
        }
        updateSaveButtonIcon();
    }
});

document.querySelector('.star-btn').addEventListener('click', function () {
    const dropdown = document.querySelector('.dropdown');
    if (dropdown.style.display === 'none' || dropdown.style.display === '') {
        dropdown.innerHTML = '';
        if (savedCities.length > 0) {
            savedCities.forEach(city => {
                const cityItem = document.createElement('div');
                cityItem.classList.add('dropdown-item');
                cityItem.textContent = city;
                cityItem.addEventListener('click', function () {
                    document.querySelector('.city-input').value = city;
                    dropdown.style.display = 'none';
                });
                dropdown.appendChild(cityItem);
            });
        } else {
            const noCityItem = document.createElement('div');
            noCityItem.classList.add('dropdown-item');
            noCityItem.textContent = 'No cities saved';
            dropdown.appendChild(noCityItem);
        }
        dropdown.style.display = 'block';
    } else {
        dropdown.style.display = 'none';
    }
});

document.addEventListener('click', function (event) {
    const dropdown = document.querySelector('.dropdown');
    const starBtn = document.querySelector('.star-btn');
    if (!starBtn.contains(event.target) && !dropdown.contains(event.target)) {
        dropdown.style.display = 'none';
    }
});

async function getFetchData(endPoint, query) {
    try {
        const apiURL = `https://api.openweathermap.org/data/2.5/${endPoint}?${query}&appid=${apiKey}&units=metric`;
        const response = await fetch(apiURL);

        if (!response.ok) {
            console.error(`Error: ${response.statusText}`);
            throw new Error(`API request failed: ${response.status}`);
        }

        return response.json();
    } catch (error) {
        console.error('Failed to fetch data:', error);
        throw error;
    }
}

function getWeatherIcon(id) {
    if (id <= 232) return 'thunderstorm.svg';
    if (id <= 321) return 'drizzle.svg';
    if (id <= 531) return 'rain.svg';
    if (id <= 622) return 'snow.svg';
    if (id <= 781) return 'atmosphere.svg';
    if (id === 800) return 'clear.svg';
    return 'clouds.svg';
}

function getCurrentDate() {
    const currentDate = new Date();
    const options = {
        weekday: 'short',
        day: '2-digit',
        month: 'short'
    };

    return currentDate.toLocaleDateString('en-GB', options);
}

function updateBackgroundImage(icon) {
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

async function updateWeatherInfo(city) {
    try {
        const weatherData = await getFetchData('weather', `q=${city}`);
        if (weatherData.cod != 200) {
            showDisplaySection(notFoundSection);
            return;
        }

        const {
            name: country,
            main: { temp, humidity },
            weather: [{ id, main }],
            wind: { speed }
        } = weatherData;

        countryTxt.textContent = country;
        tempTxt.textContent = Math.round(temp) + ' °C';
        conditionTxt.textContent = main;
        humidityValueTxt.textContent = humidity + '%';
        windValueTxt.textContent = speed + ' M/s';

        currentDateTxt.textContent = getCurrentDate();
        const weatherIcon = getWeatherIcon(id);
        weatherSummaryImg.src = `assets/weather/${weatherIcon}`;

        updateSaveButtonIcon();
        updateBackgroundImage(weatherIcon);
        await updateForecastsInfo(city);
        showDisplaySection(weatherInfoSection);
    } catch (error) {
        console.error("Failed to fetch data", error);
        showDisplaySection(notFoundSection);
    }
}

updateWeatherInfo(cityInput.value);

async function updateForecastsInfo(city) {
    try {
        const forecastsData = await getFetchData('forecast', `q=${city}`);
        const timeTaken = '12:00:00';
        const todayDate = new Date().toISOString().split('T')[0];

        forecastItemsContainer.innerHTML = '';
        let forecastCount = 0;
        const uniqueDates = new Set();

        for (let forecastWeather of forecastsData.list) {
            const forecastDate = forecastWeather.dt_txt.split(' ')[0];
            if (forecastWeather.dt_txt.includes(timeTaken) && forecastDate !== todayDate && !uniqueDates.has(forecastDate)) {
                updateForecastItems(forecastWeather);
                uniqueDates.add(forecastDate);
                forecastCount++;
                if (forecastCount === 7) break;
            }
        }
    } catch (error) {
        console.error("Failed to fetch data:", error);
    }
}

function updateForecastItems(weatherData) {
    const {
        dt_txt: date,
        weather: [{ id }],
        main: { temp }
    } = weatherData;

    const dateTaken = new Date(date);
    const dateOptions = {
        day: '2-digit',
        month: 'short'
    };

    const dateResult = dateTaken.toLocaleDateString('en-US', dateOptions);

    const forecastItem = `
        <div class="forecast-item">
            <h5 class="forecast-item-date regular-txt">${dateResult}</h5>
            <img src="assets/weather/${getWeatherIcon(id)}" class="forecast-item-img">
            <h5 class="forecast-item-temp">${Math.round(temp)} °C</h5>
        </div>
    `;
    forecastItemsContainer.insertAdjacentHTML('beforeend', forecastItem);
}

function showDisplaySection(section) {
    [weatherInfoSection, searchCitySection, notFoundSection].forEach(sec => sec.style.display = 'none');
    section.style.display = 'flex';
}

function getWeatherByLocation(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);
    fetchWeatherData(latitude, longitude);
}

function showError(error) {
    console.error('Geolocation error:', error);
}

function fetchWeatherData(lat, lon) {
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=metric&appid=${apiKey}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            document.querySelector('.country-txt').textContent = data.name;
            document.querySelector('.temp-txt').textContent = `${data.main.temp} °C`;
            document.querySelector('.condition-txt').textContent = data.weather[0].description;
            document.querySelector('.humidity-value-txt').textContent = `${data.main.humidity}%`;
            document.querySelector('.wind-speed-value-txt').textContent = `${data.wind.speed} M/s`;

            currentDateTxt.textContent = getCurrentDate();
            const weatherIcon = getWeatherIcon(data.weather[0].id);
            document.querySelector('.weather-summary-img').src = `assets/weather/${weatherIcon}`;
            updateBackgroundImage(weatherIcon);
            showDisplaySection(weatherInfoSection);
            updateForecastsInfoByCoords(lat, lon);
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);
            showDisplaySection(notFoundSection);
        });
}

async function updateForecastsInfoByCoords(lat, lon) {
    try {
        const forecastsData = await getFetchData('forecast', `lat=${lat}&lon=${lon}`);
        const timeTaken = '12:00:00';
        const todayDate = new Date().toISOString().split('T')[0];

        forecastItemsContainer.innerHTML = '';
        let forecastCount = 0;
        const uniqueDates = new Set();

        for (let forecastWeather of forecastsData.list) {
            const forecastDate = forecastWeather.dt_txt.split(' ')[0];
            if (forecastWeather.dt_txt.includes(timeTaken) && forecastDate !== todayDate && !uniqueDates.has(forecastDate)) {
                updateForecastItems(forecastWeather);
                uniqueDates.add(forecastDate);
                forecastCount++;
                if (forecastCount === 7) break;
            }
        }
    } catch (error) {
        console.error("Failed to fetch data:", error);
    }
}

const autocompleteApiKey = '0f817170f14442eeae3200106242110';
const autocompleteApiURL = `http://api.weatherapi.com/v1/search.json?key=${autocompleteApiKey}&q=`;

function clearAutocomplete() {
    const autocompleteItems = document.querySelector('.autocomplete-items');
    if (autocompleteItems) {
        autocompleteItems.remove();
    }
}

searchBtn.addEventListener('click', () => {
    if (cityInput.value.trim() !== '') {
        updateWeatherInfo(cityInput.value);
        cityInput.value = '';
        cityInput.blur();
        clearAutocomplete();
    }
});

cityInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' && cityInput.value.trim() !== '') {
        event.preventDefault();
        updateWeatherInfo(cityInput.value);
        cityInput.value = '';
        cityInput.blur();
        clearAutocomplete();
    }
});

function autocomplete(inputElement) {
    let currentFocus;

    inputElement.addEventListener('input', function () {
        const query = this.value;
        closeAllLists();

        if (!query) return;

        fetch(autocompleteApiURL + query)
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
                    item.addEventListener('click', function () {
                        inputElement.value = this.getElementsByTagName('input')[0].value;
                        clearAutocomplete();
                        closeAllLists();
                    });
                    autocompleteList.appendChild(item);
                });
            })
            .catch(error => console.error('Error fetching city data:', error));
    });

    inputElement.addEventListener('keydown', function (e) {
        let items = document.getElementById(this.id + 'autocomplete-list');
        if (items) items = items.getElementsByTagName('div');

        if (e.keyCode === 40) {
            currentFocus++;
            addActive(items);
        } else if (e.keyCode === 38) {
            currentFocus--;
            addActive(items);
        } else if (e.keyCode === 13) {
            e.preventDefault();
            if (currentFocus > -1 && items) {
                items[currentFocus].click();
            }
            clearAutocomplete();
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

    document.addEventListener('click', function (e) {
        closeAllLists(e.target);
        clearAutocomplete();
    });
}

autocomplete(document.getElementById('cityInput'));

// I have followed this tutorial to start up my coding project https://youtu.be/krUdJ87uxXc?feature=shared however I have implemented my own twist to it and have changed a lot. I did not copy the tutorial, since it does not even work. I just like the tutorial user interface.