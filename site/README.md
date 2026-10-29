# egecoskun.com (static)

Plain HTML, CSS and JS. No build step on Vercel.

- Edit sources in `src/` and run `python3 src/build.py` to regenerate `backlot/index.html` and `assets/`.
- Vercel: import `egec/backlot`, Root Directory `site`, Framework preset "Other", no build command.
- Media (videos, screenshots, prototypes) are served from GitHub Pages: https://egec.github.io/backlot/
- Type scales with the screen: 16px at 1440, 18px at 1920 (root font-size, everything in rem).
