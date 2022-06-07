# Begginer Quest

# Step -1
```
opened the link: https://cctv-web.2021.ctfcompetition.com/
```

#Step-2

```
- password was required 
- opened the source code
- go through that code
- got something intersting below there

```
# Code-part
```javascript
<script>
const checkPassword = () => {
  const v = document.getElementById("password").value;
  const p = Array.from(v).map(a => 0xCafe + a.charCodeAt(0));

  if(p[0] === 52037 &&
     p[6] === 52081 &&
     p[5] === 52063 &&
     p[1] === 52077 &&
     p[9] === 52077 &&
     p[10] === 52080 &&
     p[4] === 52046 &&
     p[3] === 52066 &&
     p[8] === 52085 &&
     p[7] === 52081 &&
     p[2] === 52077 &&
     p[11] === 52066) {
    window.location.replace(v + ".html");
  } else {
    alert("Wrong password!");
  }
}

window.addEventListener("DOMContentLoaded", () => {
  document.getElementById("go").addEventListener("click", checkPassword);
  document.getElementById("password").addEventListener("keydown", e => {
    if (e.keyCode === 13) {
      checkPassword();
    }
  });
}, false);
</script>


// // Explanation:

// - here got the password part
// - in this it was adding a hexdecimal character to each password letter
// - to we need to subtract that hexdecimal character from each password letter
// - we designed a python script to do so 
// - python script below 
```
# Step-3
```python
'''
- making the python script 
- file name: script.py
'''

offest = 0xcafe

password = {0:52037, 6:52081, 5:52063 ,1:52077 ,9:52077 ,10:52080, 4:52046 ,3:52066 ,8:52085 ,7:52081 ,2:52077 ,11:52066}

output = ""

for i in range(12):
    output += chr(password[i]-offest) # here it is just subtracting the values of dictionary with the offset 
print(output)

```

# Step-4
```
- got the ouput as: GoodPassword
- placed this password in the password filed
- got the flag: CTF{IJustHopeThisIsNotOnShodan}

!!!!! Congratulations !!!!!
```

