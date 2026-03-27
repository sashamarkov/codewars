        }
    },
    
    isWeather: {
        check: (prompt) => prompt.includes("weather"),
        execute: (prompt) => {
            const match = prompt.match(/at (\d+):(\d+)(am|pm)/);
            if (!match) return '?';
            const [_, hour, minute, period] = match;
            return bot.getWeather(parseInt(hour), parseInt(minute), period);
        }
    },
    
    add: (a, b) => a + b,
    subtract: (a, b) => b - a,
    convertTo24Hour: (hour, period) => {
        if (period === 'am' && hour === 12) {
            return 12;
        }
        if (period === 'pm' && hour === 12) {
            return 0;
        }
        if (period === 'am') {
            return hour;
        }
        return hour + 12;
    },
    getWeather: (hour, minute, period) => {
        const hour24 = bot.convertTo24Hour(hour, period);
        if (hour24 >= 6 && hour24 <= 18) {
            if (hour24 === 18 && minute > 0) {
                return "raining";
            }
            return "sunny";
        }
        return "raining";
    }
};