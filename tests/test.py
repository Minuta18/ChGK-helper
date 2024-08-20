import requests
import json

resp = requests.get('http://127.0.0.1:5000/api/v1/packages/', json={

}, headers={
    'Content-Type': 'application/json',
    'Authorization': 'ax4rqjr-JWConDxPMMNmiTzvMayo_Y1llRYdNbVklUJHZFuBo3ChXhkG7fgXHi7nsabRP7QbublT8T4OBMIzrAhTb8Yw7DGkZs5epguWM_ATYW1WlC7LQpf07XXvv95Fvjp2N4BLD3Xsa-_p3Ax1f8kOO0oSSI9xNdrlKZmyasAPwVb06mHqijIcsueaByv5m2LKz6R0',
})

print('=======================')
print(f'Status: { resp.status_code } { resp.reason }')
print(f'Result: { json.dumps(resp.json(), indent=4) }')
print('=======================')
