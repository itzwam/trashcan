

result=$(grep laCour /Applications/Slack.app/Contents/Resources/app.asar.unpacked/src/static/ssb-interop.js)
if [ -z "$result" ]; then
echo <<EOF
echo Installing 
cat >> /Applications/Slack.app/Contents/Resources/app.asar.unpacked/src/static/ssb-interop.js <<EOF
document.addEventListener('DOMContentLoaded', function() {
 $.ajax({
   url: 'https://raw.githubusercontent.com/laCour/slack-night-mode/master/css/raw/black.css',
   success: function(css) {
     $("<style></style>").appendTo('head').html(css);
   }
 });
});
EOF
else
echo Already installed
fi
