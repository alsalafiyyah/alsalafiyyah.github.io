class MediaPlayer {
	constructor(player, options) {
		this.player = player;
		this.progress = 0;

		/* defaults */
		this.volumeControls = true;
		this.seekControls = true;
	}

	render(options) {
		if (options) {
			this.extend(options);
		}

		if (this.player.controls) {
			this.player.controls = false;
		}

		this.container = this.createElement('div', {
			class: 'playr'
		});

		this.player.parentNode.insertBefore(this.container, this.player);
		this.container.appendChild(this.player);

		this.initPlayer();
		this.createUI();
		this.attachHandlers();
		this.setVolume(50);
	}

	initPlayer() {
		if (this.player.controls) {
			this.player.controls = false;
		}
		this.fileName = decodeURIComponent(this.player.src.split('/').pop());
		this.player.load();
	}

	setDimensions() {
		var _scope = this;
		_scope.uiRect = _scope.container.getBoundingClientRect();
		_scope.barRect = _scope.progressBar.getBoundingClientRect();

		if (_scope.uiRect.width < 620) {
			_scope.container.classList.add('compact');
		} else {
			_scope.container.classList.remove('compact');
		}

		if (_scope.volumeControls) {
			_scope.volRect = _scope.volumeBar.getBoundingClientRect();
		}

		_scope.barLeft = _scope.progressBar.offsetLeft;
		_scope.barWidth = _scope.progressBar.offsetWidth;

		var offsetWidth = _scope.titleBox.offsetWidth;
		var scrollWidth = _scope.titleBox.scrollWidth;

	if (scrollWidth > offsetWidth) {
		_scope.titleBox.classList.add('overflow');
		_scope.titleBox.innerHTML = '<span>' + _scope.fileName + '</span><span>' + _scope.fileName + '</span>';
	} else {
		_scope.titleBox.classList.remove('overflow');
		_scope.titleBox.innerHTML = '<span class="hide">' + _scope.fileName + '</span>';
	}
	}

	attachHandlers() {
		var _scope = this;
		this.seeking = false;
		this.dragging = false;

		/* Play */
		this.playButton.addEventListener('click', this.play.bind(this));
		this.player.addEventListener('ended', this.reset.bind(this));

		/* Progress */
		this.player.addEventListener("timeupdate", this.updateProgress.bind(this), false);
		this.player.addEventListener("loadedmetadata", this.updateProgress.bind(this), false);

		/* Seek */
		this.progressBar.parentNode.addEventListener("mousedown", function(event) {
			_scope.seeking = true;
			_scope.seek(event);
		}, false);
		window.addEventListener("mousemove", this.seek.bind(this), false);

		/* Other */
		window.addEventListener("mouseup", this.mouseUp.bind(this), false);

		/* Resize */
		var timeout = null;
		window.addEventListener('resize', function(event) {
			/* debounce */
			clearTimeout(timeout);
			timeout = setTimeout(function() {
				_scope.setDimensions();
			}, 250);
		}, false);
	}

	mouseUp(event) {
		if (this.dragging) {
			this.volX = event.clientX - this.volRect.left;
			if (this.volX >= this.volRect.width) {
				this.volX = this.volRect.width;
			} else if (this.volX <= 0) {
				this.volX = 0;
			}
			this.dragging = false;
		}
		if (this.seeking) {
			if (this.wasPlaying) {
				this.play();
				this.wasPlaying = false;
			}
			this.seeking = false;
		}
	}

	play() {
		var that = this;
		if (!!this.player.paused) {
			this.container.classList.add('playing');
			this.container.classList.remove('paused');
			this.player.play();
		} else {
			this.pause();
		}
	}

	pause() {
		if (this.player.paused) return;
		this.container.classList.add('paused');
		this.container.classList.remove('playing');
		this.player.pause();
	}

	fastForward() {
		this.player.currentTime += 5;
	}

	rewind() {
		this.player.currentTime -= 5;
	}

	seek(event) {
		if (!this.seeking) return;
		if (!this.player.paused) {
			this.wasPlaying = true;
			this.pause();
		}
		var p = (event.clientX - this.barRect.left) / this.barWidth;
		this.player.currentTime = this.player.duration * p;
	}

	seekTo(time) {
		this.player.currentTime = time;
	}

	adjustVolume(event) {
		if (!this.dragging) return;

		var scale = (event.clientX - this.volRect.left) / this.volRect.width;
		var vol = scale.toFixed(2);

		if (vol >= 1) {
			scale = vol = 1;
		} else if (vol <= 0) {
			scale = vol = 0;
		}

		this.player.volume = vol;
		this.setStyle(this.volumeBar.firstElementChild, {
			'transform': 'scale3d(' + scale + ',1,1)'
		});
	}

	setVolume(level) {
		level /= 100;
		this.player.volume = level;

		if (this.volumeControls) {
			this.setStyle(this.volumeBar.firstElementChild, {
				'transform': 'scale3d(' + level + ',1,1)'
			});
		}
	}

	updateProgress() {
		let currentTime = Math.floor(this.player.currentTime);
		let duration = Math.floor(this.player.duration);
		this.progress = currentTime / duration;
		this.setStyle(this.progressBar, {
			'transform': 'scale3d(' + this.progress + ',1,1)'
		});
		this.durationBox.innerHTML = this.format(currentTime) + ' / ' + this.format(duration);
	}

	reset() {
		this.player.currentTime = 0;
		this.updateProgress();
		this.container.classList.remove('playing');

		if (this.repeat) {
			this.play();
		}
	}

	format(seconds) {
		var time = new Date(seconds * 1000).toISOString().substr(11, 8),
			len = time.length,
			zeroes = time.slice(0, 2) == '00';
		if (zeroes) {
			return time.slice(3, len);
		}
		return time;
	}

	setStyle(element, properties) {
		var property, css = '';
		for (property in properties) {
			css += property + ': ' + properties[property] + ';';
		}
		element.style.cssText += css;
	}

	createUI() {
		var _scope = this;
		var ui = this.createElement('div', {
			class: 'playr-ui'
		});
		var controlsLeft = this.createElement('div', {
			class: 'playr-controls left'
		});
		var panel = this.createElement('div', {
			class: 'playr-panel'
		});
		var progress = this.createElement('div', {
			class: 'playr-progress'
		});

		this.titleBox = this.createElement('div', {
			class: 'playr-filename',
			html: '<span>'+_scope.fileName+'</span>'
		});

		this.durationBox = this.createElement('div', {
			class: 'playr-duration'
		});
		this.playButton = this.createElement('button', {
			class: 'playr-play',
			type: 'button'
		});
		this.progressBar = this.createElement('div', {
			class: 'playr-progress-bar'
		});
		if (this.volumeControls) {
			ui.classList.add('volume-controls');
			var controlsRight = this.createElement('div', {
				class: 'playr-controls right'
			});
			var volume = this.createElement('div', {
				class: 'playr-volume'
			});

			this.volumeBar = this.createElement('div', {
				class: 'playr-volume-box',
				html: '<span></span>'
			});

			volume.appendChild(this.volumeBar);
			controlsRight.appendChild(volume);

			this.volumeBar.addEventListener("mousedown", function(event) {
				_scope.dragging = true;
				_scope.adjustVolume(event);
			}, false);

			window.addEventListener("mousemove", this.adjustVolume.bind(this), false);
		}

		if (this.seekControls) {
			ui.classList.add('seek-controls');
			this.rwButton = this.createElement('button', {
				class: 'playr-rewind',
				type: 'button'
			});
			controlsLeft.appendChild(this.rwButton);

			this.rwButton.addEventListener("click", this.rewind.bind(this), false);
		}

		controlsLeft.appendChild(this.playButton);

		if (this.seekControls) {
			this.ffButton = this.createElement('button', {
				class: 'playr-fastforward',
				type: 'button'
			});
			controlsLeft.appendChild(this.ffButton);

			this.ffButton.addEventListener("click", this.fastForward.bind(this), false);
		}

		progress.appendChild(this.progressBar);

		panel.appendChild(progress);
		panel.appendChild(_scope.titleBox);
		panel.appendChild(_scope.durationBox);

		ui.appendChild(controlsLeft);
		ui.appendChild(panel);

		if (this.volumeControls) {
			ui.appendChild(controlsRight);
		}

		this.container.appendChild(ui);

		this.setDimensions();
	}

	createElement(a, b) {
		var c = document,
			d = c.createElement(a);
		if (b && "object" == typeof b) {
			var e;
			for (e in b)
				if ("html" === e) d.innerHTML = b[e];
				else if ("text" === e) {
				var f = c.createTextNode(b[e]);
				d.appendChild(f)
			} else d.setAttribute(e, b[e])
		}
		return d
	}

	extend(options) {
		var option;
		for (option in options) {
			this[option] = options[option];
		}
	}
}
player = new MediaPlayer(document.getElementById('player'));
player.render({
	// seekControls: false,
	// volumeControls: false
});
