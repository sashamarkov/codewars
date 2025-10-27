function whoWon(players, extraCard, extraTakers) {
    const cardValue = card => isNaN(card) ? 10 : +card;
    const extraValue = cardValue(extraCard);
    
    return Object.entries(players)
        .map(([name, cards]) => [
            name, 
            cards.split(', ').reduce((sum, card) => sum + cardValue(card), 0) + 
            (extraTakers.includes(name) ? extraValue : 0)
        ])
        .sort(([nameA, scoreA], [nameB, scoreB]) => {
            const validA = scoreA <= 21;
            const validB = scoreB <= 21;
            if (validA && validB) {
                if (scoreA !== scoreB) return scoreB - scoreA;
                return nameA.localeCompare(nameB);
            }
            if (validA && !validB) return -1;
            if (!validA && validB) return 1;
            if (scoreA !== scoreB) return scoreA - scoreB;
            return nameA.localeCompare(nameB);
        });
}