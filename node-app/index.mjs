import fs from 'fs'

fs.appendFile('my.file.txt', 'Файл создан Node.js',
(err)=> {if (err) throw err
console.log('File save!')
})

setTimeout( ()=> console.log('Конец'), 30000)