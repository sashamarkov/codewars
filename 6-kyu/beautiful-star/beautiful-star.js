function makestar(s) {
  const rows = [[], [], []];
  for (let i = 0; i < s.length; i++) {
    rows[0].push('* * *');
    rows[1].push(`* ${s[i]} *`);
    rows[2].push('* * *');
  }
  const starString = rows.map(row => row.join('  ')).join('\n');
  const escaped = starString.replace(/\n/g, '<br>').replace(/ /g, '&nbsp;');
  return '<div id="blink">TEXT HERE</div> <script language="javascript"> function changeColor(){ var color="#f00|#0f0|#00f|#880|#808|#088|yellow|green|blue|gray"; color=color.split("|"); document.getElementById("blink").style.color=color[parseInt(Math.random() * color.length)]; } setInterval("changeColor()",500); </script>'.replace('TEXT HERE', escaped);
}