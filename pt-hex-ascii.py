      ## This script converts RSA plain text(pt) to ascii for root flag.
python3
pt = 24604052029401386049980296953784287079059245867880966944246662849341507003750
str(hex(pt))
      ## '0x3665666331613564626238393034373531636536353636613330356262386566'
      ## Getting rid of 0x
str(hex(pt)[2:])
      ## '3665666331613564626238393034373531636536353636613330356262386566'

hex_string = '3665666331613564626238393034373531636536353636613330356262386566'
      ##Convert hex string to bytes
byte_data = bytes.fromhex(hex_string)
      ## Decode bytes to ASCII string
ascii_string = byte_data.decode('ascii')

print (ascii_string)
## 6efthisistherootflagef
