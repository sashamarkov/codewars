async function getLeaderboardHonor() {
    const response = await fetch('https://www.codewars.com/users/leaderboard');
    const html = await response.text();
    const honors = [];
    const regex = /<td class="honor">([\d,]+)<\/td>/g;
    let match;
    while ((match = regex.exec(html)) !== null) {
        honors.push(parseInt(match[1].replace(/,/g, '')));
    }
    return honors.sort((a, b) => b - a).slice(0, 500);
}