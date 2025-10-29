# MindAR Image Tracking Web App

A web application that uses MindAR.js to track images and play videos on top of them using augmented reality.

## 🚀 Features

- **Image Tracking**: Uses MindAR.js for real-time image tracking
- **Video Overlay**: Plays videos on top of tracked images
- **Modern UI**: Beautiful gradient design with smooth transitions
- **Camera Integration**: Real-time AR using device camera
- **Cross-platform**: Works on desktop and mobile devices

## 📋 Prerequisites

Before you start, you'll need:

1. A target image (for tracking)
2. A video file (to display on the tracked image)
3. A local web server (required for camera access)

## 🛠️ Setup Instructions

### Step 1: Prepare Assets

You need to create two asset files:

1. **Target Image** - The image that will be tracked
2. **MindAR Target File** - The tracking data file

#### Creating the MindAR Target File:

1. Go to [https://hiukim.github.io/mind-ar-js/tools/compile/](https://hiukim.github.io/mind-ar-js/tools/compile/)
2. Upload your target image
3. Download the generated `.mind` file
4. Rename it to `target.mind` and place it in the `assets/` folder

#### Video File:

- Place your video file (mp4 recommended) in the `assets/` folder
- Update the filename in `index.html` line 133 if needed

### Step 2: Start Local Server

AR applications require HTTPS or localhost to access the camera. Use one of these methods:

#### Option A: Using Python

```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

#### Option B: Using Node.js (http-server)

```bash
npx http-server
```

#### Option C: Using VS Code Live Server Extension

If you use VS Code, install the "Live Server" extension and click "Go Live".

### Step 3: Open in Browser

Navigate to:
```
http://localhost:8000
```

## 📁 Project Structure

```
.
├── index.html          # Main HTML file
├── README.md           # This file
└── assets/            # Your assets go here
    ├── target.mind    # MindAR tracking file (you need to create this)
    └── video.mp4      # Video file to play (add your video)
```

## 🎯 How to Use

1. **Prepare Target Image**: Print or display the target image
2. **Start AR**: Click the "Start AR" button
3. **Allow Camera**: Grant camera permissions when prompted
4. **Point Camera**: Point your device camera at the target image
5. **Watch Video**: Video will appear on top of the tracked image
6. **Stop AR**: Click "Stop AR" when done

## 🎨 Customization

### Change Video

Edit line 133 in `index.html`:
```html
<a-video src="assets/your-video.mp4" ...>
```

### Adjust Video Position/Size

Edit the video properties in `index.html`:
```html
<a-video 
    src="assets/video.mp4"
    position="0 0 0"      <!-- x y z position -->
    rotation="0 0 0"      <!-- x y z rotation -->
    width="1.6"           <!-- width multiplier -->
    height="0.9"          <!-- height multiplier -->
    ...>
```

### Change Video Behavior

- `autoplay="true"` - Auto-play video
- `loop="true"` - Loop video
- `playsinline="true"` - Play inline on mobile

## 🌐 Browser Compatibility

- Chrome (recommended)
- Firefox
- Edge
- Safari (iOS Safari with some limitations)

## 📱 Mobile Use

This app works on mobile devices! Best results on:
- Latest Android phones
- iPhones (iOS 11+)

Note: iPhone users may need to enable autoplay settings for video.

## 🔧 Troubleshooting

### Camera not working
- Ensure you're using `localhost` or HTTPS
- Grant camera permissions
- Check browser console for errors

### Video not playing
- Ensure video format is supported (mp4 recommended)
- Check video codec (H.264/AAC recommended)
- Enable autoplay in browser settings (for iPhone)

### Target not tracking
- Ensure good lighting
- Hold target steady
- Make sure target is clearly visible
- Reduce distance from target

## 📚 Resources

- [MindAR.js Documentation](https://hiukim.github.io/mind-ar-js-doc/)
- [A-Frame Documentation](https://aframe.io/docs/)
- [MindAR Target Compiler](https://hiukim.github.io/mind-ar-js/tools/compile/)

## 🎓 Learning

Want to customize further? Learn about:
- **A-Frame Entities**: [A-Frame Entity Documentation](https://aframe.io/docs/)
- **MindAR Component**: [MindAR Image Tracking](https://hiukim.github.io/mind-ar-js-doc/)
- **Video Attributes**: [A-Frame Video Component](https://aframe.io/docs/)

## 🌐 GitHub Pages Deployment

This project is ready for GitHub Pages deployment!

### Quick Deploy:

1. **Push to GitHub** (see PUSH_INSTRUCTIONS.md for authentication help)
2. **Enable GitHub Pages**:
   - Go to repository Settings → Pages
   - Source: `main` branch, `/ (root)` folder
   - Save
3. **Access your site**: `https://younuzbn.github.io/mindar/`

### Notes:
- ✅ HTTPS is automatically provided by GitHub Pages
- ✅ All assets (video.mp4, target.mind) are included
- ✅ `.nojekyll` file ensures proper file serving
- ✅ Works on mobile devices too!

## 📝 License

This project is for educational purposes. MindAR.js is an open-source project.

## 🤝 Contributing

Feel free to fork and customize this project for your needs!

## ⚠️ Important Notes

- Always serve over HTTPS or localhost for camera access
- Ensure good lighting for best tracking results
- High contrast target images work best
- Keep the target image stable for accurate tracking

