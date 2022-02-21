



command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

# Получу списки вланов для каждой переменной. Запишу полученные строки в переменные.
command1_vlans = command1.split(' ')[-1]
command2_vlans = command2.split(' ')[-1]
# command1_vlans = command1_vlans.replace(',', ' ')
# command2_vlans = command2_vlans.replace(',', ' ')

# # Для исклюкчения повторяэющихся элементов преобразую списки в множества
uniq_vlans_set = set(command1_vlans) & set(command2_vlans)
uniq_vlans_list = list(uniq_vlans_set)
uniq_vlans_list = uniq_vlans_list.remove(',')
print(uniq_vlans_list)