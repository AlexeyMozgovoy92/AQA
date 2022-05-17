class RegParser:
    ADDRESS_REGEX = (
        r'^(?:[A-Z][a-z]+,\s)?'
        r'(?:[A-Z][a-z]+(?:\s[Cc]ity)?,\s)?'
        r'[-\w\s]+\w(?:\sstr\.)?,\s'
        r'\d+\s*[-/\\,|]\s*\d+$'
    )

    CONTACT_REGEX = (
        r'^(?:(?:(?:name=(?P<name>[A-Za-z0-9 -]+))|'
        r'(?:age=(?P<age>[A-Za-z0-9 -]+))|'
        r'(?:city=(?P<city>[A-Za-z0-9 -]+))|'
        r'(?:surname=(?P<surname>[A-Za-z0-9 -]+)))(?:;|$)){1,4}(?<!;)$'
    )

    PRICE_REGEX = r'(?:(?<=[\$€] )\d+(?:[\.,]\d+)?)|(?:\d+(?:[\.,]\d+)?(?= *BYN))'

    @classmethod
    def _find_addresses(cls, string):
        return re.findall(cls.ADDRESS_REGEX, string, flags=re.MULTILINE)

    @classmethod
    def _find_contacts(cls, string, regex_num):
        result = []

        for match in re.finditer(cls.CONTACT_REGEX, string, flags=re.MULTILINE):
            result.append({
                key: value
                for key, value in match.groupdict().items()
            })

        return result

    @classmethod
    def _find_prices(cls, string):
        result = []

        for match in re.finditer(cls.PRICE_REGEX, string, flags=re.MULTILINE):
            num = match.group()
            if ',' in num or '.' in num:
                num = float(num.replace(',', '.'))
            else:
                num = int(num)
            result.append(num)

        return result

    @classmethod
    def find(cls, string, regex_num):
        if regex_num == 1:
            return cls._find_addresses(string)
        elif regex_num == 2:
            return cls._find_contacts(string)
        else:
            return cls._find_prices(string)
