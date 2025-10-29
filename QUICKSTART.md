# 🚀 Quick Start Guide

Get your MindAR Image Tracking app running in 5 minutes!

## Step 1: Create Your MindAR Target File

1. Open your browser and go to: https://hiukim.github.io/mind-ar-js/tools/compile/
2. Click "Upload" to upload a target image (JPG or PNG)
   - **Tip**: Use an image with high contrast and clear features
   - **Recommended**: Posters, logos, or printed images work best
3. Wait for processing (usually takes 1-2 minutes)
4. Click "Download" to download the `.mind` file
5. Rename the downloaded file to `target.mind`
6. Place it in the `assets/` folder of this project

## Step 2: Add Your Video

1. Prepare a video file (MP4 recommended)
2. Rename it to `video.mp4` 
3. Place it in the `assets/` folder

**Recommended Video Settings:**
- Format: MP4 (H.264 codec)
- Size: Keep under 20MB for faster loading
- Resolution: 1280x720 or 1920x1080
- Keep it short: 10-30 seconds for best performance

## Step 3: Start the Server

Open your terminal in the project folder and run:

```bash
# Using Python 3
python3 -m http.server 8000

# Or using Python 2
python -m SimpleHTTPServer 8000

# Or using Node.js (if you have it installed)
npx http-server
```

## Step 4: Open in Browser

1. Open your browser (Chrome recommended)
2. Go to: `http://localhost:8000`
3. You should see the app interface!

## Step 5: Use the AR App

1. Print or display the same image you uploaded to MindAR
2. Click "Start AR" in the app
3. Allow camera permissions
4. Point your camera at the target image
5. Watch the video appear! 🎬

## 📱 Testing Tips

- **Desktop**: Test with your webcam
- **Mobile**: Open `http://your-computer-ip:8000` on your phone
- **Best Results**: 
  - Good lighting
  - Stable target image
  - Clear, high contrast image
  - Hold camera 30-60cm from target

## 🎯 Troubleshooting

**"Camera not working"**
- Make sure you're using localhost or HTTPS
- Grant camera permissions
- Check if another app is using the camera

**"Video not appearing"**
- Make sure the target image matches exactly
- Ensure good lighting
- Try moving closer/farther from target

**"Tracking not smooth"**
- Better lighting
- Reduce camera shake
- Use a printed version of target image

## 🎨 Next Steps

Now that it's working, customize it:

1. **Change the Video**: Edit `index.html` line 133
2. **Adjust Position**: Modify the `position` attribute
3. **Change Size**: Modify `width` and `height` attributes
4. **Add Multiple Targets**: Add more `<a-entity>` tags

Have fun! 🚀

