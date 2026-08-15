const cacheName = 'alsalafiyyah-v1.1';
const assets = [
  '/',
  '/index.md',
  '/assets/custom-styles.css',
  '/assets/icons/web-app-manifest-192x192.png',
  '/assets/icons/web-app-manifest-512x512.png'
];

self.addEventListener('install', event => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(cacheName).then(cache => {
      console.log('Caching shell assets');
      return cache.addAll(assets);
    })
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(key => key !== cacheName)
            .map(key => caches.delete(key))
      );
    })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    fetch(event.request)
      .then(networkResponse => {
        // If we have internet, return the fresh version
        return networkResponse;
      })
      .catch(() => {
        // If internet fails, look in the cache
        return caches.match(event.request);
      })
  );
});