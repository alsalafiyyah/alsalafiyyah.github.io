---
layout: page
title: "Privacy Policy"
permalink: /privacy-policy/
---

  <script type="text/javascript" src="https://identity.netlify.com/v1/netlify-identity-widget.js"></script>

    <!-- Logged-Out View -->
    <div id="logged-out-view" class="space-y-6">
      <div class="w-16 h-16 bg-indigo-50 text-indigo-600 rounded-full flex items-center justify-center mx-auto mb-4">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-8 h-8">
          <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" />
        </svg>
      </div>

      <div class="space-y-2">
        <h1 class="text-2xl font-bold tracking-tight text-slate-900">Login</h1>
      </div>

      <button 
        id="login-btn" 
        class="w-full bg-indigo-600 hover:bg-indigo-700 active:bg-indigo-800 text-white font-medium py-3 px-4 rounded-xl transition duration-200 ease-in-out shadow-sm shadow-indigo-200 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
      >
        Log In
      </button>
    </div>

    <!-- Logged-In View (Hidden by default) -->
    <div id="logged-in-view" class="hidden space-y-6">
      <div class="w-16 h-16 bg-emerald-50 text-emerald-600 rounded-full flex items-center justify-center mx-auto mb-4">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-8 h-8">
          <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
      </div>

      <div class="space-y-2">
        <h2 class="text-2xl font-bold tracking-tight text-slate-900">
          Hello, <span id="user-name" class="text-indigo-600">User</span>!
        </h2>
        <p class="text-sm text-slate-500">You are currently logged into your account.</p>
      </div>

      <button 
        id="logout-btn" 
        class="w-full bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium py-3 px-4 rounded-xl transition duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-slate-400 focus:ring-offset-2"
      >
        Log Out
      </button>
    </div>

  <script>
    // Get HTML elements
    const loginBtn = document.getElementById('login-btn');
    const logoutBtn = document.getElementById('logout-btn');
    const loggedOutView = document.getElementById('logged-out-view');
    const loggedInView = document.getElementById('logged-in-view');
    const userName = document.getElementById('user-name');

    // 1. Open the login modal when clicking the login button
    loginBtn.addEventListener('click', () => netlifyIdentity.open('login'));

    // 2. Trigger logout when clicking the logout button
    logoutBtn.addEventListener('click', () => netlifyIdentity.logout());

    // 3. Listen for the 'init' event to check if a user is already logged in
    netlifyIdentity.on('init', (user) => {
      updateUI(user);
    });

    // 4. Listen for successful logins
    netlifyIdentity.on('login', (user) => {
      updateUI(user);
      netlifyIdentity.close(); // Close the modal
    });

    // 5. Listen for logouts
    netlifyIdentity.on('logout', () => {
      updateUI(null);
    });

    // Helper function to update the user interface dynamically using Tailwind's 'hidden' class
    function updateUI(user) {
      if (user) {
        loggedOutView.classList.add('hidden');
        loggedInView.classList.remove('hidden');
        userName.textContent = user.user_metadata?.full_name || user.email;
      } else {
        loggedOutView.classList.remove('hidden');
        loggedInView.classList.add('hidden');
      }
    }
  </script>
