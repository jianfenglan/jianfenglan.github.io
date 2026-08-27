(function () {
  function splitTimelineMeta() {
    var items = document.querySelectorAll('.news-list .news-meta');

    items.forEach(function (meta) {
      if (meta.dataset.timelineSplit === 'true') return;

      var text = (meta.textContent || '').trim();
      var parts = text.split(/\s*·\s*/);
      if (parts.length < 2) return;

      var dateText = parts.shift().trim();
      var placeText = parts.join(' · ').trim();

      var date = document.createElement('span');
      date.className = 'news-meta-date';
      date.textContent = dateText;

      var separator = document.createElement('span');
      separator.className = 'news-meta-separator';
      separator.textContent = ' · ';

      var place = document.createElement('span');
      place.className = 'news-meta-place';
      place.textContent = placeText;

      meta.textContent = '';
      meta.appendChild(date);
      meta.appendChild(separator);
      meta.appendChild(place);
      meta.dataset.timelineSplit = 'true';
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', splitTimelineMeta, { once: true });
  } else {
    splitTimelineMeta();
  }
})();
