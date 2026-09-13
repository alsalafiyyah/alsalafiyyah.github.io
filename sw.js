const cacheName = 'alsalafiyyah-v1.1';
const assets = [
  '/',
  '/index.html',
  '/assets/css/main.css',
  '/assets/icons/web-app-manifest-192x192.png',
  '/assets/icons/web-app-manifest-512x512.png'
];

// Install Event: Caching app shell
self.addEventListener('install', event => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(cacheName).then(cache => {
      console.log('Caching shell assets');
      return cache.addAll(assets);
    })
  );
});

// Activate Event: Clear old outdated caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(key => key !== cacheName)
            .map(key => caches.delete(key))
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch Event: Cache-First Strategy with Network Fallback
self.addEventListener('fetch', event => {
  // Skip non-GET requests (like browser extensions or POST forms)
  if (event.request.method !== 'GET') return;

  event.respondWith(
    caches.match(event.request).then(cachedResponse => {
      // Return cached version if found, otherwise fetch from network
      return cachedResponse || fetch(event.request).then(networkResponse => {
        // Optional: dynamically cache new fetched assets if valid
        return caches.open(cacheName).then(cache => {
          if (networkResponse.status === 200) {
            cache.put(event.request, networkResponse.clone());
          }
          return networkResponse;
        });
      }).catch(() => {
        // Fallback for offline page navigation if needed
        if (event.request.headers.get('accept').includes('text/html')) {
          return caches.match('/');
        }
      });
    })
  );
});