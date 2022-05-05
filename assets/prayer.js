/*
* Name: jquery-prayer-times
* Author: Muhammad Mabrouk
* NPM: https://www.npmjs.com/package/jquery-prayer-times
* GitHub: https://github.com/MuhammadMabrouk/jquery-prayer-times
*/
$.fn.prayerTimes = function(options = {}) {
  const $this = this;
  const prayersList = [
    "Ø§Ù„ÙØ¬Ø±",
    "Ø§Ù„Ø´Ø±ÙˆÙ‚",
    "Ø§Ù„Ø¸Ù‡Ø±",
    "Ø§Ù„Ø¹ØµØ±",
    "Ø§Ù„ØºØ±ÙˆØ¨",
    "Ø§Ù„Ù…ØºØ±Ø¨",
    "Ø§Ù„Ø¹Ø´Ø§Ø¡",
    "Ø§Ù„Ø¥Ù…Ø³Ø§Ùƒ",
    "Ù…Ù†ØªØµÙ Ø§Ù„Ù„ÙŠÙ„"
  ];
  const defaultOptions = {
    method: typeof options.method === 'undefined' ? 4 : options.method,
    school: typeof options.school === 'undefined' ? 0 : options.school,
    city: options.city || null,
    country: options.country || null,
    imsak: typeof options.imsak === 'undefined' ? true : options.imsak,
    sunrise: typeof options.sunrise === 'undefined' ? true : options.sunrise,
    sunset: typeof options.sunset === 'undefined' ? true : options.sunset,
    midnight: typeof options.midnight === 'undefined' ? true : options.midnight,
    arabic: typeof options.arabic === 'undefined' ? false : options.arabic,
    militaryTime: typeof options.militaryTime === 'undefined' ? true : options.militaryTime,
    outputEl: options.outputEl || 'table'
  };
  const savedData = JSON.parse(localStorage.getItem('jquery-prayer-times'));

  // get prayer times
  function getPrayerTimes({city, country}) {
    const url = `https://api.aladhan.com/v1/timingsByCity?midnightMode=1&method=${defaultOptions.method}&school=${defaultOptions.school}&city=${city}&country=${country}`;

    // get data if first time or new day or different queries
    if (!savedData || (savedData && (compareTime(savedData.timestamp) > 0 || url !== savedData.lastQueries))) {
      $.get(url, res => {
        // save in localStorage
        localStorage.setItem('jquery-prayer-times', JSON.stringify({
          lastQueries: url,
          value: res,
          timestamp: getFormattedDate()
        }));

        // generate output content
        $this.html(generateOutput(res.data.timings));
      });

    } else {

      // generate output content
      $this.html(generateOutput(savedData.value.data.timings));
    }
  }

  // generate output content
  function generateOutput(timings) {
    const container = (defaultOptions.outputEl === 'table') ? 'table' : 'ul';
    const isArabic = defaultOptions.arabic ? true : false;
    const is12Hr = defaultOptions.militaryTime ? false : true;
    const name = (time, index) => isArabic ? prayersList[index] : time;
    const formattedTime = (time) => is12Hr ? timeTo12HrFormat(time) : time;

    let i = 0;
    let content = `<${container}>`;
    for (const time in timings) {
      const timeName = name(time, i);
      const timeValue = formattedTime(timings[time]);
      if (!defaultOptions.imsak && time === 'Imsak') { i++; continue; };
      if (!defaultOptions.sunrise && time === 'Sunrise') { i++; continue; };
      if (!defaultOptions.sunset && time === 'Sunset') { i++; continue; };
      if (!defaultOptions.midnight && time === 'Midnight') { i++; continue; };

      content += `${container === 'table' ?
        `<tr tabindex="0"><td>${timeName}</td><td>${timeValue}</td></tr>` :
        `<li tabindex="0"><span>${timeName}</span><span>${timeValue}</span></li>`}`;
      i++;
    }
    content += `</${container}>`;

    return content;
  }

  // get date in nice format (return today's date by default)
  function getFormattedDate(date = new Date()) {
    const dd = String(date.getDate()).padStart(2, '0');
    const mm = String(date.getMonth() + 1).padStart(2, '0'); // January is 0!
    const yyyy = date.getFullYear();
    const getFormattedDate = `${dd}/${mm}/${yyyy}`;
  
    return getFormattedDate;
  }

  // calculate the number of days between two dates
  function compareTime(time) {
    const todayDate = new Date(...getFormattedDate().split('/'));
    const oldDate = new Date(...time.split('/'));
    // hours * minutes * seconds * milliseconds
    const oneDay = 24 * 60 * 60 * 1000;
  
    return Math.round(((todayDate - oldDate) / oneDay) / 365);
  }

  // convert time from 24 hour to 12 hour format
  function timeTo12HrFormat(time) {
    const timeArr = time.split(':');
    const H = +timeArr[0];
    const h = H % 12 || 12;
    const am_pm = (H < 12 || H === 24) ? 'AM' : 'PM';
    return `${`${h}`.padStart(2, '0')}:${timeArr[1]} ${am_pm}`;
  }

  // call 'getPrayerTimes' function
  if (defaultOptions.city && defaultOptions.country) {
    getPrayerTimes({city: defaultOptions.city, country: defaultOptions.country});

    // if same day
  } else if (savedData && (compareTime(savedData.timestamp) === 0)) {
    const parameters = new URLSearchParams(savedData.lastQueries);
    getPrayerTimes({city: parameters.get('city'), country: parameters.get('country')});

  } else {
    $.get("https://ipinfo.io/json", data => getPrayerTimes({ city: data.city, country: data.country }));
  }
}
