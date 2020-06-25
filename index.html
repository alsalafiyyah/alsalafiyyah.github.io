<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>Alifta Fatwas</title>
<style>
.icons {
 color: #007bff;
}
i {
 color: #007bff;
}
*:hover,
*:focus,
*:active
 {
  outline: none;
  box-shadow: none !important;
  -webkit-appearance: none;
}
.container {
 margin-top: 30px;
 margin-bottom: 40px;
}
.border-radius-0 {
 border-radius: 0! important;
}
.lists {
 margin-top: 20px;
}
.form-text {
 margin-bottom: 10px;
}
</style>
  </head>
  <body>
    <div class="container ">
        <form id="search_form" autocomplete="off">
        <nav class="navbar navbar-light bg-light border-radius-0">
        <small class="form-text text-muted">Instagram: <a href="https://instagram.com/Alsalafiyyah" target="_blank">@Alsalafiyyah</a></small>
            <input type="search" placeholder="Search a fatwa" id="search_input" class="form-control input-group border border-right-0 border border-left-0 border-top-0 border-radius-0">
        </nav>
        </form>
      <div class="lists"><ul id="list" class="list-group border-radius-0"></ul></div>
    </div>
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <script>
      const filterFiles = (filter) => {
        filter = filter.toLowerCase()
        return (file) => {
          const filePath = file.path;
          const fileName = filePath.replace('.md', '').toLowerCase().replace(/-/g, '');
          const isMarkdown = (/.md$/).test(filePath);
          const isNotLicense = filePath !== 'LICENSE.md';
          const isInFilter = filter.split(' ')
            .every((token) => fileName.indexOf(token.toLowerCase()) !== -1)
          return isMarkdown && isNotLicense && isInFilter;
        }
      }
      const matchScore = (file, filter) => {
        const fileWords = file.name.replace('.md', '').toLowerCase().split('-');
        filter = filter.toLowerCase()
        let wordIndex;
        let letterPosition;
        for (wordIndex = 0; wordIndex < fileWords.length; wordIndex++) {
          letterPosition = fileWords[wordIndex].indexOf(filter)
          if (letterPosition > -1) break;
        }
        if (letterPosition < 0) {
          letterPosition = 100;
        }
        return wordIndex + letterPosition * 100;
      }
      const sortFiles = (filter) => {
        filter = filter.toLowerCase()
        return (fileA, fileB) => {
          return matchScore(fileA, filter) < matchScore(fileB, filter) ? -1 : 1;
        }
      }
      const updateList = (data, filter = '') => {
        let htmlString = '';
        for (let file of data.filter(filterFiles(filter)).sort(sortFiles(filter))) {
          const fileName = file.name.replace('.md', '');
          const filePath = file.path.replace('.md', '');
          const fileDisplayName = fileName.split('-').join(' ');
          htmlString += `<li class="list-group-item border-radius-0 border-0"><i class="far fa-folder icons"></i> <a href="${filePath}">${fileDisplayName}</a></li>`;
        }
        document.getElementById('list').innerHTML = htmlString;
      }
      const navigateToFile = (data, filter = '') => {
        files = data.filter(filterFiles(filter));
        if (files.length === 1) {
          const fileName = files[0].path.replace('.md', '');
          document.location = fileName;
        }
      }
      (async () => {
        const response = await fetch('https://api.github.com/repos/alsalafiyyah/alsalafiyyah.github.io/contents/alifta');
        const data = await response.json();
        const search_form = document.getElementById('search_form');
        const search_input = document.getElementById('search_input');
        const search_value = decodeURIComponent(document.location.search.replace('?', '').replace(/\+/g, ' '));
        search_input.value = search_value;
        navigateToFile(data, search_value);
        updateList(data, search_value);
        search_form.addEventListener('submit', (event) => {
          event.preventDefault();
          navigateToFile(data, search_input.value);
        })
        search_input.addEventListener('input', (event) => {
          updateList(data, event.target.value);
        })
        document.addEventListener('keypress', (event) => {
          search_input.focus()
        })
      })()
      // Register service worker
      if (navigator.serviceWorker && !navigator.serviceWorker.controller) {
        navigator.serviceWorker.register('./serviceworker.js');
      }
    </script>
  </body>
</html>
