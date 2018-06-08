const Request = require('request');

const Axios = require('axios');

const Fs = require('fs');

const url = 'http://18h.animezilla.com/manga';

const dirs = './imgs';

let fileName = url.split('/');

fileName = fileName[fileName.length-1];

let dir = `${dirs}/${fileName}`


// referer用于防治盗链，随意加上该站点地址就可以   --检查不是很严格
var options = {
        url: url,  
        method: 'GET', 
        headers: {  
            'Cookie': 'Hm_lvt_8e2a116daf0104a78d601f40a45c75b4=1528271911,1528364306,1528387612,1528421683; Hm_lpvt_8e2a116daf0104a78d601f40a45c75b4=1528421697',
            'Connection': 'keep-alive',
            'Host': '18h.animezilla.com',
            'Upgrade-Insecure-Requests': 1,
            'Reffer': 'http://18h.animezilla.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9, image/webp,image/apng, */*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }//伪造请求头  
    };  

// Axios({method: 'get',url: url,responseType: 'stream'}).then(function (response) {
//         response.data.pipe(Fs.createWriteStream(dir))
// });
// Request(options, (res, data)=>{
//     console.log(res, data)
// })
Request(options).pipe(Fs.createWriteStream(dir).on('close', ()=>{
    console.log('save')
})).on('error', (e)=>{
    console.log(e)
});


