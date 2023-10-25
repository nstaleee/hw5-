from pywebio.input import input as pw_input, slider, FLOAT
from pywebio.output import put_success

ONE_KILO_CALORIE = 0.32541

ENERGY_OSTRICH_EGG = 118
ENERGY_RABBIT = 197
ENERGY_SEA_BASS = 123
ENERGY_SWEET_RED_PEPPER = 26
ENERGY_PARSLEY = 45
ENERGY_BANANA = 87
ENERGY_WAFFLES = 425
ENERGY_BREAD = 246
ENERGY_PISTACHIOS = 555
ENERGY_KEFIR = 51

total_energy = 0
summa = 0
portion_ostrich_egg = pw_input(f'Введіть бажану порцію страусиних яєць 🥚, грам '
                               f'Калорійність {ENERGY_OSTRICH_EGG} кКал/100гр', type=FLOAT)
sum1 = ONE_KILO_CALORIE * ENERGY_OSTRICH_EGG * portion_ostrich_egg
summa += sum1
portion_ostrich_egg_energy = (float(portion_ostrich_egg) * ENERGY_OSTRICH_EGG) / 100
total_energy = total_energy + portion_ostrich_egg_energy
put_success(f'Ви замовили {portion_ostrich_egg} грамів стаусиних яєць 🥚,\n'
            f'Калорійнісь порції {portion_ostrich_egg}\n'
            f'Загальна накопичена калорійність замовлення: {total_energy},\n'
            f'До сплати {sum1} грн')

portion_rabbit = slider(f'Введіть бажану порцію кролика 🐇, грам '
                               f'Калорійність {ENERGY_RABBIT} кКал/100гр', min_value=0, max_value=2500)
sum2 = ONE_KILO_CALORIE * ENERGY_RABBIT * portion_rabbit + sum1
portion_rabbit_energy = (float(portion_rabbit) * ENERGY_RABBIT) / 100
total_energy = total_energy + portion_rabbit_energy
put_success(f'Ви замовили {portion_rabbit} грамів кролика 🐇,\n'
            f'Калорійнісь порції {portion_rabbit}\n'
            f'Загальна накопичена калорійність замовлення: {total_energy},\n'
            f'До сплати {sum2} грн')

portion_sea_bass = slider(f'Введіть бажану порцію окуня 🐟, грам '
                          f'Калорійність {ENERGY_SEA_BASS} кКал/100гр', min_value=0, max_value=2500)
sum3 = ONE_KILO_CALORIE * ENERGY_SEA_BASS * portion_sea_bass + sum2
portion_sea_bass_energy = (float(portion_sea_bass) * ENERGY_SEA_BASS) / 100
total_energy = total_energy + portion_sea_bass_energy
put_success(f'Ви замовили {portion_sea_bass} грамів окуня 🐟,\n'
            f'Калорійнісь порції {portion_sea_bass}\n'
            f'Загальна накопичена калорійність замовлення: {total_energy},\n'
            f'До сплати {sum3} грн')

portion_sweet_red_pepper = pw_input(f'Введіть бажану порцію перцю 🫑, грам '
                               f'Калорійність {ENERGY_SWEET_RED_PEPPER} кКал/100гр', type=FLOAT)
sum4 = ONE_KILO_CALORIE * ENERGY_SWEET_RED_PEPPER * portion_sweet_red_pepper + sum3
portion_sweet_red_pepper_energy = (float(portion_sweet_red_pepper) * ENERGY_SWEET_RED_PEPPER) / 100
total_energy = total_energy + portion_sweet_red_pepper_energy
put_success(f'Ви замовили {portion_sweet_red_pepper} грамів перцю 🫑,\n'
            f'Калорійнісь порції {portion_sweet_red_pepper}\n'
            f'Загальна накопичена калорійність замовлення: {total_energy},\n'
            f'До сплати {sum4} грн')

portion_parsley = pw_input(f'Введіть бажану порцію пучков петрушки 🥬, грам '
                               f'Калорійність {ENERGY_PARSLEY} кКал/100гр', type=FLOAT)
sum5 = ONE_KILO_CALORIE * ENERGY_PARSLEY * portion_parsley + sum4
portion_parsley_energy = (float(portion_parsley) * ENERGY_PARSLEY) / 100
total_energy = total_energy + portion_parsley_energy
put_success(f'Ви замовили {portion_parsley} пучков петрушки 🥬,\n'
            f'Калорійнісь порції {portion_parsley}\n'
            f'Загальна накопичена калорійність замовлення: {total_energy},\n'
            f'До сплати {sum5} грн')

portion_banana = pw_input(f'Введіть бажану порцію бананів 🍌, грам '
                               f'Калорійність {ENERGY_BANANA} кКал/100гр', type=FLOAT)
sum6 = ONE_KILO_CALORIE * ENERGY_BANANA * portion_banana + sum5
portion_banana_energy = (float(portion_banana) * ENERGY_BANANA) / 100
total_energy = total_energy + portion_banana_energy
put_success(f'Ви замовили {portion_banana} грамів бананів 🍌,\n'
            f'Калорійнісь порції {portion_banana}\n'
            f'Загальна накопичена калорійність замовлення: {total_energy},\n'
            f'До сплати {sum6} грн')

portion_waffles = pw_input(f'Введіть бажану порцію вафель 🧇, грам '
                               f'Калорійність {ENERGY_WAFFLES} кКал/100гр', type=FLOAT)
sum7 = ONE_KILO_CALORIE * ENERGY_WAFFLES * portion_waffles + sum6
portion_waffles_energy = (float(portion_waffles) * ENERGY_WAFFLES) / 100
total_energy = total_energy + portion_waffles_energy
put_success(f'Ви замовили {portion_waffles} грамів вафель 🧇,\n'
            f'Калорійнісь порції {portion_waffles}\n'
            f'Загальна накопичена калорійність замовлення: {total_energy},\n'
            f'До сплати {sum7} грн')

portion_bread = pw_input(f'Введіть бажану порцію хліба 🍞, грам '
                               f'Калорійність {ENERGY_BREAD} кКал/100гр', type=FLOAT)
sum8 = ONE_KILO_CALORIE * ENERGY_BREAD * portion_bread + sum7
portion_bread_energy = (float(portion_bread) * ENERGY_BREAD) / 100
total_energy = total_energy + portion_bread_energy
put_success(f'Ви замовили {portion_bread} грамів хліба 🍞,\n'
            f'Калорійнісь порції {portion_bread}\n'
            f'Загальна накопичена калорійність замовлення: {total_energy},\n'
            f'До сплати {sum8} грн')

portion_pistachios = slider(f'Введіть бажану порцію фісташок 🥜, грам '
                          f'Калорійність {ENERGY_PISTACHIOS} кКал/100гр', min_value=0, max_value=2500)
sum9 = ONE_KILO_CALORIE * ENERGY_PISTACHIOS * portion_pistachios + sum8
portion_pistachios_energy = (float(portion_pistachios) * ENERGY_PISTACHIOS) / 100
total_energy = total_energy + portion_pistachios_energy
put_success(f'Ви замовили {portion_pistachios} грамів фісташок 🥜,\n'
            f'Калорійнісь порції {portion_pistachios}\n'
            f'Загальна накопичена калорійність замовлення: {total_energy},\n'
            f'До сплати {sum9} грн')

portion_kefir = slider(f'Введіть бажану порцію кефіру 🥛, мілілітрів '
                          f'Калорійність {ENERGY_KEFIR} кКал/100мл', min_value=0, max_value=2500)
sum10 = ONE_KILO_CALORIE * ENERGY_KEFIR * portion_kefir + sum9
portion_kefir_energy = (float(portion_kefir) * ENERGY_KEFIR) / 100
total_energy = total_energy + portion_kefir_energy
put_success(f'Ви замовили {portion_kefir} мілілітрів кефіру 🥛,\n'
            f'Калорійнісь порції {portion_kefir}\n'
            f'Загальна накопичена калорійність замовлення: {total_energy},\n'
            f'До сплати {sum10} грн')

sum = sum1 + sum2 + sum3 + sum4 + sum5 + sum6 + sum7 + sum8 + sum9 + sum10

if sum < 1000:
    put_success(f'Я досі голодний 😔')
if sum < 1500:
    put_success(f'Я ситий 😊')
if sum > 1500:
    put_success(f'Я наївся, але переплатив, їжа залишилась 😠')

put_success(f'Всього до сплати {sum10} грн')