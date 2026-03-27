    buildAverageRow() {
        if (this.isEmpty) return this;
        this.averageRow = [
            `|${'The average score'.padEnd(this.nameW)}|${this._formatScoreCell(this.avg)}|`,
            this._line()
        ];
        return this;
    }
    
    build() {
        if (this.isEmpty) return '';
        return [...this.header, ...this.studentRows, ...this.averageRow].join('\n');
    }
}
​
function formatScoreList(list) {
    return new ScoreTableBuilder(list)
        .buildHeader()
        .buildStudentRows()
        .buildAverageRow()
        .build();
}