
const handleArgs = () => {
  if (process.argv.length > 3){
    throw 'too many arguments';
  }
  if (process.argv.length < 2){
    throw 'You need to provide one more argument';
  }

  sentence = process.argv[2];
  return sentence;
}

const http = require('http');

sentence_to_translate = handleArgs();


const data = JSON.stringify({
  sentence: sentence_to_translate 
})

const options = {
  hostname: 'localhost',
  port: 4000,
  path: '/translate',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  }
}

const req = http.request(options, res => {
  res.on('data', d => {
    process.stdout.write(d)
  })
})

req.on('error', error => {
  console.error(error)
})

req.write(data)
req.end()
