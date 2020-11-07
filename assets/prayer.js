this.ignoreTimes = ['Sunrise', 'Sunset', 'Midnight'];
this.hijriMonths = {
 1: "Muharram",
 2: "Safar",
 3: "Rabi' Al-Awwal",
 4: "Rabi' Al-Thani",
 5: "Juma Al-Awwal",
 6: "Juma Al-Thani",
 7: "Rajab",
 8: "Sha'ban",
 9: "Ramadan",
 10: "Shawwal",
 11: "Dhul Qi'dah",
 12: "Dhul-Hijjah"
};
init();
function init() {
 this.prayerData = JSON.parse(window.localStorage.getItem('prayerData'));
 if (this.prayerData && this.prayerData.date) {
  var nowDate = new Date();
  var thenDate = new Date(this.prayerData.date);
  if (
   nowDate.getYear() > thenDate.getYear() ||
   nowDate.getMonth() > thenDate.getMonth() ||
   nowDate.getDate() > thenDate.getDate()
  ) {
    fetchDataPrayer()
   } else {
    fillData(this.prayerData.data);
   }
 } else {
  fetchDataPrayer();
 }
}


function fetchDataPrayer() {
 fetch('https://api.pray.zone/v2/times/today.json?city=taif')
  .then(response => {
    return response.json()
  })
  .then(data => {
    // Work with JSON data here
    if (data.code === 200) {
     window.localStorage.setItem('prayerData', JSON.stringify({'date': new Date(), 'data': data}));
     fillData(data);
    }
  })
  .catch(err => {
    // Do something for an error here
  })
}

function fillData(data) {
 var hijriDate = data.results.datetime[0].date.hijri;
 var times = data.results.datetime[0].times;
 fillPrayerTable(times);
 fillHijriDate(hijriDate);
}

function fillPrayerTable(times) {
  var id = 1;
  var currentD = new Date();
  var options = {
     timeZone: 'Asia/Riyadh',
     hour: 'numeric', minute: 'numeric', second: 'numeric',
  },
     formatter = new Intl.DateTimeFormat([], options);
  var currentTime = formatter.format(new Date());
  var currentTimeArr = currentTime.split(':');
  currentD.setHours(currentTimeArr[0], currentTimeArr[1], currentTimeArr[2]);
  var nextPrayerFound = false;
  for (var index in times) {
   if (this.ignoreTimes.includes(index)) {
    continue;
   }
   var timeElement = document.getElementById(id + '-time');
   var nameElement = document.getElementById(id + '-name');
   nameElement.innerText = index;
   timeElement.innerText = times[index];
   var prayerTime = new Date();
   var timesArr = times[index].split(':');
   prayerTime.setHours(timesArr[0],timesArr[1],0);
   if (!nextPrayerFound && prayerTime >= currentD) {
    var secondsLeft = parseInt((prayerTime - currentD)/1000);
    nextPrayerFound = true;
    nameElement.parentElement.parentElement.style.background = 'cyan';
    timeElement.innerText += ' (Next prayer)';
    var previousId = id - 1;
    if (previousId === 0) {
     previousId = 6;
    }
    var previousTimeElement = document.getElementById(previousId + '-time');
    var previousNameElement = document.getElementById(previousId + '-name');
    nextPrayerTime(secondsLeft, timeElement, previousTimeElement);
    previousTimeElement.parentElement.parentElement.style.background = 'yellow';
    previousTimeElement.innerText += ' (Passed prayer)';
   }
   id ++;
  }
}

function nextPrayerTime(secondsLeft, element, previousElement)
{
 var span = document.createElement('span');
 element.appendChild(span);
 var interval = setInterval(function() {
  if (secondsLeft > 0) {
   var hours = String(parseInt(secondsLeft / 3600)).padStart(2, '0'); 
   var minutes = String(parseInt((secondsLeft - (hours * 3600)) / 60)).padStart(2, '0');
   var seconds = String(parseInt(secondsLeft % 60)).padStart(2, '0');
   span.innerText = ' ' + hours + ':' + minutes + ':' + seconds;
   secondsLeft--;
  } else {
   clearInterval(interval);
   previousElement.parentElement.parentElement.style.background = 'transparent';
   element.appendChild(span);
   init();
  }
 }, 1000
 )
 
}

function fillHijriDate(date) {
 var dateSplitted = date.split('-');
 var dateStr = 'Not available for the moment';
 if (dateSplitted.length === 3) {
  dateStr = dateSplitted[2] + ' ' + this.hijriMonths[parseInt(dateSplitted[1])] + ' ' + dateSplitted[0];
 }
 document.getElementById('hijri-date').innerText = dateStr;
}