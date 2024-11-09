function updateCountdown() {
    fetch('/countdown')
        .then(response => response.json())
        .then(data => {
            document.getElementById('days-together').textContent = data.days_together;
            document.getElementById('days-since-special').textContent = data.days_since_special;

            // 更新第 N 个 100 天倒计时
            document.getElementById('next-100-days-count').textContent = data.next_100_days.days;
            document.getElementById('next-100-days').textContent = formatCountdown(data.next_100_days.countdown);

            // 更新第 N 周年倒计时
            document.getElementById('next-anniversary-count').textContent = data.next_anniversary.year;
            document.getElementById('next-anniversary').textContent = formatCountdown(data.next_anniversary.countdown);

            // 更新特殊纪念日第 N 个 100 天倒计时
            document.getElementById('next-100-special-days-count').textContent = data.next_100_special_days.days;
            document.getElementById('next-100-special-days').textContent = formatCountdown(data.next_100_special_days.countdown);

            // 更新特殊纪念日第 N 周年倒计时
            document.getElementById('next-special-anniversary-count').textContent = data.next_special_anniversary.year;
            document.getElementById('next-special-anniversary').textContent = formatCountdown(data.next_special_anniversary.countdown);
        });
}

function formatCountdown(seconds) {
    if (seconds === null) return '已过期';
    let d = Math.floor(seconds / (24 * 3600));
    let h = Math.floor((seconds % (24 * 3600)) / 3600);
    let m = Math.floor((seconds % 3600) / 60);
    let s = seconds % 60;
    return `${d}天 ${h}小时 ${m}分钟 ${s}秒`;
}

// 每秒刷新倒计时
setInterval(updateCountdown, 1000);
