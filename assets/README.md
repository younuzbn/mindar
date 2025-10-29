# Assets Folder

Place your assets here:

## Required Files

1. **target.mind** - Your MindAR tracking data file
   - Create this by uploading your target image at: https://hiukim.github.io/mind-ar-js/tools/compile/
   - Download the `.mind` file and rename it to `target.mind`

2. **video.mp4** - Your video file to display on the tracked image
   - Recommended: mp4 format with H.264 codec
   - Keep file size reasonable for faster loading

## Example Structure

```
assets/
├── README.md        (this file)
├── target.mind      (MindAR tracking data)
└── video.mp4        (Your video file)
```

## Tips

- Use high-contrast images for better tracking
- Keep videos under 50MB for faster loading
- Ensure videos are in a web-compatible format
- Test with different video resolutions for best results

