
def test():
    passport_data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    byr:1937 iyr:2017 cid:147 hgt:183cm
    ujftkrebdtikjgclufhdlfribirhffcd
    iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    hcl:#cfa07d byr:1929
    
    hcl:#ae17e1 iyr:2013
    eyr:2024
    ecl:brn pid:760753108 byr:1931
    hgt:179cm
    
    hcl:#cfa07d eyr:2025 pid:166559648
    iyr:2011 ecl:brn hgt:59in"""

    passport_data = passport_data.split("\n\n")

    valid_passports = 0

    for passport in passport_data:
        # print(passport)
        if ('byr' in passport and 'iyr' in passport and 'eyr' in passport and
                'hgt' in passport and 'hcl' in passport and 'ecl' in passport and
                'pid' in passport):
            # print(passport)

            stripped_passport = passport.strip(" ").replace("\n" ," ").split(" ")
            passport_dict = {}


            for x in stripped_passport:
                x = x.split(":")
                print(x)
                passport_dict[x[0]] = x[1]

            byr = int(passport_dict['byr'])
            iyr = int(passport_dict['iyr'])
            eyr = int(passport_dict['eyr'])

            hgt = passport_dict['hgt']
            if (('cm' in hgt and 150 <= int(hgt.split('cm')[0]) <= 193) or
                    ('in' in hgt and 59 <= int(hgt.split('in')[0]) <= 76)):
                hgt = True
            else:
                hgt = False

            hcl = passport_dict['hcl']
            print(hcl)
            if hcl[0] == '#' and len(x) == 7:
                print('Passed: hash and len')
                for x in hcl[1:]:

                    if x in [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,0 ,'a' ,'b' ,'c' ,'d' ,'e' ,'f']:
                        hcl = True
                    else:
                        hcl = False
                        break
            else:
                hcl = False

            ecl = passport_dict['ecl']
            if ecl in ["amb", "blu", "brn", "gry", "grn", "hzloth"]:
                ecl = True
            else:
                ecl = False

            pid = passport_dict['pid']

            for x in pid:
                if x in [0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]:
                    pid = True
                else:
                    pid = False
                    break

            # byr (Birth Year) - four digits; at least 1920 and at most 2002.
            # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
            # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
            # hgt (Height) - a number followed by either cm or in:
            # If cm, the number must be at least 150 and at most 193.
            # If in, the number must be at least 59 and at most 76.
            # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
            # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
            # pid (Passport ID) - a nine-digit number, including leading zeroes.
            # cid (Country ID) - ignored, missing or not.

            print(byr, iyr, eyr, hgt, hcl, ecl, pid)
            if(1920 <= byr <= 2002 and
                    1920 <= iyr <= 2002 and
                    2020 <= eyr <= 2030 and
                    hgt and hcl and ecl and pid):
                valid_passports += 1

            print(passport_dict)


    print(valid_passports)
    # passport_data[0].replace("\n"," ").split(" ")

if __name__ == '__main__':
    test()

