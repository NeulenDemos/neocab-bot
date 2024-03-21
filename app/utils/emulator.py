from app import misc

student = (
    'richard.brown@khpi.edu.ua',
    'demo',
    777,
    'en',
    1,
    'CIP',
)


def get(url, **kwargs):
    params = kwargs.get('params')
    if url == misc.api_cab:
        if params.get('page') == 1:
            return [{
                'fakultet': "Educational and Scientific Institute of Computer Sciences and Information Technologies",
                'fam': "Brown",
                'fid': 21,
                'gid': "1",
                'grupa': "CEP-919d",
                'imya': "Richard",
                'kafedra': "Computer Engineering and Programming",
                'kid': 51,
                'kurs': 4,
                'oplata': "Budget",
                'osvitprog': "Modern programming, mobile devices and computer games",
                'otch': "Edgar",
                'sezon': 1,
                'speciality': "Computer Engineering",
                'specialization': "Programming of Mobile Devices and Computer Games",
                'st_cod': "777",
                'train_form': "Full-time",
                'train_level': "Bachelor",
                'year': 2023,
            }]
        if params.get('page') == 2:
            return [
                {
                    'control': 'Е',
                    'credit': '4.00',
                    'data': '',
                    'if_hvost': '',
                    'indzav': 'Р',
                    'kabr': 'CEP',
                    'kafedra': 'Computer Engineering and Programming',
                    'oc_bol': '85',
                    'oc_ects': 'B',
                    'oc_id': 11316613,
                    'oc_naz': 0,
                    'oc_short': 4,
                    'prepod': 'John M. S.',
                    'subject': 'Designing mobile applications',
                },
                {
                    'control': 'З',
                    'credit': '6.00',
                    'data': '',
                    'if_hvost': '',
                    'indzav': 'З',
                    'kabr': 'CEP',
                    'kafedra': 'Computer Engineering and Programming',
                    'oc_bol': '90',
                    'oc_ects': 'A',
                    'oc_id': 11316614,
                    'oc_naz': 0,
                    'oc_short': 5,
                    'prepod': 'Maria I. R.',
                    'subject': 'Software testing',
                },
                {
                    'control': 'З',
                    'credit': '5.00',
                    'data': '',
                    'if_hvost': '',
                    'indzav': 'З',
                    'kabr': 'AIADA',
                    'kafedra': 'Artificial Intelligence and Data Analysis',
                    'oc_bol': '95',
                    'oc_ects': 'A',
                    'oc_id': 11316615,
                    'oc_naz': 0,
                    'oc_short': 5,
                    'prepod': 'David J. L.',
                    'subject': 'Artificial intelligence',
                },
                {
                    'control': 'Е',
                    'credit': '6.00',
                    'data': '',
                    'if_hvost': '',
                    'indzav': 'Р',
                    'kabr': 'CSAN',
                    'kafedra': 'Computer Systems and Networks',
                    'oc_bol': '78',
                    'oc_ects': 'C',
                    'oc_id': 11316616,
                    'oc_naz': 0,
                    'oc_short': 4,
                    'prepod': 'Ana L. G.',
                    'subject': 'Data structures',
                },
                {
                    'control': 'З',
                    'credit': '5.00',
                    'data': '',
                    'if_hvost': '',
                    'indzav': 'З',
                    'kabr': 'CSAN',
                    'kafedra': 'Computer Systems and Networks',
                    'oc_bol': '97',
                    'oc_ects': 'A',
                    'oc_id': 11316617,
                    'oc_naz': 0,
                    'oc_short': 5,
                    'prepod': 'Robert T. B.',
                    'subject': 'Database management',
                },
                {
                    'control': 'Е',
                    'credit': '3.00',
                    'data': '',
                    'if_hvost': '',
                    'indzav': 'Р',
                    'kabr': 'IOTACC',
                    'kafedra': 'Internet of Things and Automated Control Systems',
                    'oc_bol': '100',
                    'oc_ects': 'A',
                    'oc_id': 11316618,
                    'oc_naz': 0,
                    'oc_short': 5,
                    'prepod': 'Laura C. H.',
                    'subject': 'Computer networks',
                },
                {
                    'control': 'З',
                    'credit': '5.00',
                    'data': '',
                    'if_hvost': '24.02.2022',
                    'indzav': 'З',
                    'kabr': 'SEAWD',
                    'kafedra': 'Software Engineering and Web Development',
                    'oc_bol': '95',
                    'oc_ects': 'A',
                    'oc_id': 11316619,
                    'oc_naz': 0,
                    'oc_short': 5,
                    'prepod': 'Michael X. C.',
                    'subject': 'Web development',
                },
                {
                    'control': 'Е',
                    'credit': '6.00',
                    'data': '',
                    'if_hvost': '',
                    'indzav': 'З',
                    'kabr': 'FLAT',
                    'kafedra': 'Foreign Languages and Translation',
                    'oc_bol': '95',
                    'oc_ects': 'A',
                    'oc_id': 11316620,
                    'oc_naz': 0,
                    'oc_short': 5,
                    'prepod': 'Joseph K. W.',
                    'subject': 'Foreign language',
                },
                {
                    'control': 'З',
                    'credit': '5.00',
                    'data': '',
                    'if_hvost': '',
                    'indzav': 'З',
                    'kabr': 'SPAN',
                    'kafedra': 'Semiconductor Physics and Nanotechnology',
                    'oc_bol': '78',
                    'oc_ects': 'C',
                    'oc_id': 11316621,
                    'oc_naz': 0,
                    'oc_short': 4,
                    'prepod': 'Claudia E. F.',
                    'subject': 'Physics',
                },
            ]
        if params.get('page') == 5:
            return [
                {
                    'fio': "Emily O. W.",
                    'gabr': "CEP-919d",
                    'n': 1,
                    'sbal5': 5,
                    'sbal100': 95.00,
                    'studid': 224146,
                },
                {
                    'fio': "Michael W. D.",
                    'gabr': "CEP-919d",
                    'n': 2,
                    'sbal5': 5,
                    'sbal100': 92.00,
                    'studid': 224147,
                },
                {
                    'fio': "Sophia A. R.",
                    'gabr': "CEP-919d",
                    'n': 3,
                    'sbal5': 5,
                    'sbal100': 90.23,
                    'studid': 224148,
                },
                {
                    'fio': "Jacob I. M.",
                    'gabr': "CEP-919d",
                    'n': 4,
                    'sbal5': 5,
                    'sbal100': 90.23,
                    'studid': 224149,
                },
                {
                    'fio': "Isabella M. H.",
                    'gabr': "CEP-919d",
                    'n': 5,
                    'sbal5': 4,
                    'sbal100': 89.73,
                    'studid': 224150,
                },
                {
                    'fio': "Ethan E. G.",
                    'gabr': "CEP-919d",
                    'n': 6,
                    'sbal5': 4,
                    'sbal100': 89.34,
                    'studid': 224151,
                },
                {
                    'fio': "Mia A. P.",
                    'gabr': "CEP-919d",
                    'n': 7,
                    'sbal5': 4,
                    'sbal100': 89.16,
                    'studid': 224152,
                },
                {
                    'fio': "William E. S.",
                    'gabr': "CEP-919d",
                    'n': 8,
                    'sbal5': 4,
                    'sbal100': 89.01,
                    'studid': 224153,
                },
                {
                    'fio': "Abigail M. R.",
                    'gabr': "CEP-919d",
                    'n': 9,
                    'sbal5': 4,
                    'sbal100': 88.83,
                    'studid': 224154,
                },
                {
                    'fio': "Madison A. T.",
                    'gabr': "CEP-920d",
                    'n': 10,
                    'sbal5': 4,
                    'sbal100': 88.35,
                    'studid': 224155,
                },
                {
                    'fio': "Avery A. G.",
                    'gabr': "CEP-920d",
                    'n': 11,
                    'sbal5': 4,
                    'sbal100': 88.29,
                    'studid': 224156,
                },
                {
                    'fio': "Amelia H. D.",
                    'gabr': "CEP-920d",
                    'n': 12,
                    'sbal5': 4,
                    'sbal100': 87.96,
                    'studid': 224157,
                },
                {
                    'fio': "Harper E. R.",
                    'gabr': "CEP-920d",
                    'n': 13,
                    'sbal5': 4,
                    'sbal100': 87.88,
                    'studid': 224158,
                },
                {
                    'fio': "Evelyn A. S.",
                    'gabr': "CEP-920d",
                    'n': 14,
                    'sbal5': 4,
                    'sbal100': 87.66,
                    'studid': 224159,
                },
                {
                    'fio': "Aria C. J.",
                    'gabr': "CEP-920d",
                    'n': 15,
                    'sbal5': 4,
                    'sbal100': 87.63,
                    'studid': 224160,
                },
                {
                    'fio': "Chloe C. M.",
                    'gabr': "CEP-920d",
                    'n': 16,
                    'sbal5': 4,
                    'sbal100': 87.51,
                    'studid': 224161,
                },
                {
                    'fio': "Camila P. C.",
                    'gabr': "CEP-920d",
                    'n': 17,
                    'sbal5': 4,
                    'sbal100': 86,
                    'studid': 224162,
                },
                {
                    'fio': "Penelope R. C.",
                    'gabr': "CEP-920d",
                    'n': 18,
                    'sbal5': 4,
                    'sbal100': 86,
                    'studid': 224163,
                },
                {
                    'fio': "Riley L. D.",
                    'gabr': "CEP-920d",
                    'n': 19,
                    'sbal5': 4,
                    'sbal100': 86,
                    'studid': 224164,
                },
                {
                    'fio': "Layla A. O.",
                    'gabr': "CEP-921d",
                    'n': 20,
                    'sbal5': 4,
                    'sbal100': 86,
                    'studid': 224165,
                },
                {
                    'fio': "Aaliyah N. C.",
                    'gabr': "CEP-921d",
                    'n': 21,
                    'sbal5': 4,
                    'sbal100': 84,
                    'studid': 224166,
                },
                {
                    'fio': "Nora A. M.",
                    'gabr': "CEP-921d",
                    'n': 22,
                    'sbal5': 4,
                    'sbal100': 83,
                    'studid': 224167,
                },
                {
                    'fio': "Ariana S. G.",
                    'gabr': "CEP-921d",
                    'n': 23,
                    'sbal5': 4,
                    'sbal100': 83,
                    'studid': 224168,
                },
                {
                    'fio': "Skylar E. R.",
                    'gabr': "CEP-921d",
                    'n': 24,
                    'sbal5': 4,
                    'sbal100': 82,
                    'studid': 224169,
                },
                {
                    'fio': "Ellie P. E.",
                    'gabr': "CEP-921d",
                    'n': 25,
                    'sbal5': 4,
                    'sbal100': 82,
                    'studid': 224170,
                },
                {
                    'fio': "Paisley J. V.",
                    'gabr': "CEP-921d",
                    'n': 26,
                    'sbal5': 4,
                    'sbal100': 82,
                    'studid': 224171,
                },
                {
                    'fio': "Josie M. B.",
                    'gabr': "CEP-921d",
                    'n': 27,
                    'sbal5': 4,
                    'sbal100': 80,
                    'studid': 224172,
                },
                {
                    'fio': "Mila A. R.",
                    'gabr': "CEP-921d",
                    'n': 28,
                    'sbal5': 4,
                    'sbal100': 79,
                    'studid': 224173,
                },
                {
                    'fio': "Richard E. B.",
                    'gabr': "CEP-919d",
                    'n': 29,
                    'sbal5': 4,
                    'sbal100': 78,
                    'studid': 777,
                },
                {
                    'fio': "Adalyn D. G.",
                    'gabr': "CEP-921d",
                    'n': 30,
                    'sbal5': 4,
                    'sbal100': 78,
                    'studid': 224175,
                },
                {
                    'fio': "Jacob W. S.",
                    'gabr': "CSN-919d",
                    'n': 31,
                    'sbal5': 4,
                    'sbal100': 78,
                    'studid': 224176,
                },
                {
                    'fio': "Lucia C. S.",
                    'gabr': "CSN-920d",
                    'n': 32,
                    'sbal5': 4,
                    'sbal100': 78,
                    'studid': 224177,
                },
                {
                    'fio': "Willow C. G.",
                    'gabr': "CSN-919d",
                    'n': 33,
                    'sbal5': 4,
                    'sbal100': 77,
                    'studid': 224178,
                },
                {
                    'fio': "Charlotte M. M.",
                    'gabr': "CSN-919d",
                    'n': 34,
                    'sbal5': 4,
                    'sbal100': 75,
                    'studid': 224179,
                },
                {
                    'fio': "Melanie A. G.",
                    'gabr': "CSN-919d",
                    'n': 35,
                    'sbal5': 3,
                    'sbal100': 74,
                    'studid': 224180,
                },
                {
                    'fio': "Aubree L. S.",
                    'gabr': "CSN-919d",
                    'n': 36,
                    'sbal5': 3,
                    'sbal100': 72,
                    'studid': 224181,
                },
                {
                    'fio': "Lila R. V.",
                    'gabr': "CSN-919d",
                    'n': 37,
                    'sbal5': 3,
                    'sbal100': 72,
                    'studid': 224182,
                },
                {
                    'fio': "Regina E. A.",
                    'gabr': "CSN-919d",
                    'n': 38,
                    'sbal5': 3,
                    'sbal100': 71,
                    'studid': 224183,
                },
                {
                    'fio': "Eliza E. M.",
                    'gabr': "CSN-919d",
                    'n': 39,
                    'sbal5': 3,
                    'sbal100': 71,
                    'studid': 224184,
                },
                {
                    'fio': "Callie N. V.",
                    'gabr': "CSN-920d",
                    'n': 40,
                    'sbal5': 3,
                    'sbal100': 70,
                    'studid': 224185,
                },
                {
                    'fio': "Elena J. C.",
                    'gabr': "CSN-919d",
                    'n': 41,
                    'sbal5': 3,
                    'sbal100': 67,
                    'studid': 224186,
                },
                {
                    'fio': "Natalia N. C.",
                    'gabr': "CSN-920d",
                    'n': 42,
                    'sbal5': 3,
                    'sbal100': 64,
                    'studid': 224187,
                },
                {
                    'fio': "Juliette J. V.",
                    'gabr': "CSN-919d",
                    'n': 43,
                    'sbal5': 3,
                    'sbal100': 64,
                    'studid': 224188,
                },
                {
                    'fio': "Julianna Z. C.",
                    'gabr': "CSN-920d",
                    'n': 44,
                    'sbal5': 3,
                    'sbal100': 63,
                    'studid': 224189,
                },
                {
                    'fio': "Nayeli A. V.",
                    'gabr': "CSN-920d",
                    'n': 45,
                    'sbal5': 3,
                    'sbal100': 63,
                    'studid': 224190,
                },
                {
                    'fio': "Alina A. E.",
                    'gabr': "CSN-920d",
                    'n': 46,
                    'sbal5': 3,
                    'sbal100': 62,
                    'studid': 224191,
                },
                {
                    'fio': "Adeline A. C.",
                    'gabr': "CSN-920d",
                    'n': 47,
                    'sbal5': 3,
                    'sbal100': 61,
                    'studid': 224192,
                },
                {
                    'fio': "Ariya D. F.",
                    'gabr': "CSN-920d",
                    'n': 48,
                    'sbal5': 3,
                    'sbal100': 60,
                    'studid': 224193,
                },
                {
                    'fio': "Daleyza E. S.",
                    'gabr': "CSN-921d",
                    'n': 49,
                    'sbal5': 3,
                    'sbal100': 60,
                    'studid': 224194,
                },
                {
                    'fio': "Elliana E. R.",
                    'gabr': "CSN-921d",
                    'n': 50,
                    'sbal5': 2,
                    'sbal100': 59,
                    'studid': 224195,
                },
            ]
        if params.get('page') == 4:
            return [
                {
                    'audit': '5.00',
                    'control': 'Е',
                    'credit': '4.00',
                    'indzav': 'Р',
                    'kabr': 'IOTACC',
                    'kafedra': 'Internet of Things and Cloud Computing',
                    'kurs': '4',
                    'semestr': '8',
                    'subj_id': '501096',
                    'subject': 'Computer networks',
                },
                {
                    'audit': '4.00',
                    'control': 'З',
                    'credit': '3.00',
                    'indzav': 'З',
                    'kabr': 'SEAWD',
                    'kafedra': 'Software Engineering and Web Development',
                    'kurs': '4',
                    'semestr': '8',
                    'subj_id': '501097',
                    'subject': 'Web development',
                },
                {
                    'audit': '3.00',
                    'control': 'З',
                    'credit': '5.00',
                    'indzav': 'Р',
                    'kabr': 'CGAVRD',
                    'kafedra': 'Computer Graphics and Virtual Reality',
                    'kurs': '4',
                    'semestr': '8',
                    'subj_id': '501098',
                    'subject': 'Computer graphics',
                },
                {
                    'audit': '6.00',
                    'control': 'Е',
                    'credit': '4.00',
                    'indzav': 'Р',
                    'kabr': 'CAIP',
                    'kafedra': 'Computer Architecture and Information Processing',
                    'kurs': '4',
                    'semestr': '8',
                    'subj_id': '501099',
                    'subject': 'Computer architecture',
                },
                {
                    'audit': '5.00',
                    'control': 'З',
                    'credit': '3.00',
                    'indzav': 'З',
                    'kabr': 'ESP',
                    'kafedra': 'Embedded Systems Programming',
                    'kurs': '4',
                    'semestr': '8',
                    'subj_id': '501100',
                    'subject': 'Operating systems',
                },
                {
                    'audit': '6.00',
                    'control': 'Е',
                    'credit': '4.00',
                    'indzav': 'Р',
                    'kabr': 'CAIP',
                    'kafedra': 'Computer Architecture and Information Processing',
                    'kurs': '4',
                    'semestr': '8',
                    'subj_id': '501101',
                    'subject': 'Computer security',
                },
                {
                    'audit': '3.00',
                    'control': 'З',
                    'credit': '3.00',
                    'indzav': 'З',
                    'kabr': 'CGAVRD',
                    'kafedra': 'Computer Graphics and Virtual Reality',
                    'kurs': '4',
                    'semestr': '8',
                    'subj_id': '501102',
                    'subject': 'Computer vision',
                },
                {
                    'audit': '6.00',
                    'control': 'Е',
                    'credit': '4.00',
                    'indzav': 'Р',
                    'kabr': 'FLAT',
                    'kafedra': 'Foreign Languages and Translation',
                    'kurs': '4',
                    'semestr': '8',
                    'subj_id': '501103',
                    'subject': 'Foreign language',
                },
                {
                    'audit': '5.00',
                    'control': 'З',
                    'credit': '3.00',
                    'indzav': 'З',
                    'kabr': 'SPAN',
                    'kafedra': 'Semiconductor Physics and Nanotechnology',
                    'kurs': '4',
                    'semestr': '8',
                    'subj_id': '501104',
                    'subject': 'Physics',
                },
            ]
        if params.get('page') == 3:
            return [
                {
                    'subject': 'Web development',
                    'prepod': 'Michael X. C.',
                    'data': '24.02.2022',
                },
            ]
        if params.get('page') == 3:
            return [
                {
                    'dog_name': '2846',
                    'start_date': '01.09.2020',
                    'dog_price': '3000',
                    'term_start': '1',
                    'paid_date': '01.09.2020',
                    'paid_value': '2100',
                    'dp_id': 46124,
                },
                {
                    'term_start': '2',
                    'paid_date': '01.01.2021',
                    'paid_value': '2300',
                    'dp_id': 46125,
                },
                {
                    'term_start': '3',
                    'paid_date': '01.09.2021',
                    'paid_value': '2500',
                    'dp_id': 46126,
                },
                {
                    'term_start': '4',
                    'paid_date': '01.01.2022',
                    'paid_value': '2600',
                    'dp_id': 46127,
                },
                {
                    'term_start': '5',
                    'paid_date': '01.09.2022',
                    'paid_value': '2600',
                    'dp_id': 46128,
                },
                {
                    'term_start': '6',
                    'paid_date': '01.01.2023',
                    'paid_value': '2600',
                    'dp_id': 46129,
                },
                {
                    'term_start': '7',
                    'paid_date': '01.09.2023',
                    'paid_value': '2800',
                    'dp_id': 46129,
                },
                {
                    'term_start': '8',
                    'paid_date': '01.01.2024',
                    'paid_value': '3000',
                    'dp_id': 46130,
                },
            ]
    if url == misc.api_sched:
        return {
            'Monday': {
                'Para1': {
                    'Name': '',
                },
                'Para2': {
                    'Name': 'Computer networks',
                    'Aud': '101',
                    'vid': 'Lecture',
                    'Prepod': 'Laura C. H.'
                },
                'Para3': {
                    'Name': 'Foreign language',
                    'Aud': '551',
                    'vid': 'Practice',
                    'Prepod': 'Joseph K. W.'
                },
                'Para4': {
                    'Name': 'Web development',
                    'Aud': '668',
                    'vid': 'Practice',
                    'Prepod': 'Michael X. C.'
                },
                'Para5': {
                    'Name': '',
                },
                'Para6': {
                    'Name': '',
                },
            },
            'Tuesday': {
                'Para1': {
                    'Name': 'Computer graphics',
                    'Aud': '375',
                    'vid': 'Lecture',
                    'Prepod': 'Sofia V. T.'
                },
                'Para2': {
                    'Name': 'Computer architecture',
                    'Aud': '322',
                    'vid': 'Practice',
                    'Prepod': 'William T. N.'
                },
                'Para3': {
                    'Name': 'Operating systems',
                    'Aud': '413',
                    'vid': 'Lecture',
                    'Prepod': 'Isabella A. R.'
                },
                'Para4': {
                    'Name': 'Physics',
                    'Aud': '364',
                    'vid': 'Practice',
                    'Prepod': 'Claudia E. F.'
                },
                'Para5': {
                    'Name': '',
                },
                'Para6': {
                    'Name': '',
                },
            },
            'Wednesday': {
                'Para1': {
                    'Name': 'Data structures',
                    'Aud': '613',
                    'vid': 'Lecture',
                    'Prepod': 'Ana L. G.'
                },
                'Para2': {
                    'Name': 'Computer security',
                    'Aud': '143',
                    'vid': 'Lecture',
                    'Prepod': 'Daniel J. K.'
                },
                'Para3': {
                    'Name': 'Computer vision',
                    'Aud': '273',
                    'vid': 'Practice',
                    'Prepod': 'Marta P. S.'
                },
                'Para4': {
                    'Name': '',
                },
                'Para5': {
                    'Name': '',
                },
                'Para6': {
                    'Name': '',
                },
            },
            'Thursday': {
                'Para1': {
                    'Name': 'Web development',
                    'Aud': '668',
                    'vid': 'Lecture',
                    'Prepod': 'Michael X. C.'
                },
                'Para2': {
                    'Name': 'Foreign language',
                    'Aud': '551',
                    'vid': 'Practice',
                    'Prepod': 'Joseph K. W.'
                },
                'Para3': {
                    'Name': '',
                },
                'Para4': {
                    'Name': '',
                },
                'Para5': {
                    'Name': '',
                },
                'Para6': {
                    'Name': '',
                },
            },
            'Friday': {
                'Para1': {
                    'Name': 'Computer networks',
                    'Aud': '101',
                    'vid': 'Practice',
                    'Prepod': 'Laura C. H.'
                },
                'Para2': {
                    'Name': 'Computer architecture',
                    'Aud': '322',
                    'vid': 'Lecture',
                    'Prepod': 'William T. N.'
                },
                'Para3': {
                    'Name': 'Computer security',
                    'Aud': '143',
                    'vid': 'Practice',
                    'Prepod': 'Daniel J. K.'
                },
                'Para4': {
                    'Name': 'Computer graphics',
                    'Aud': '375',
                    'vid': 'Practice',
                    'Prepod': 'Sofia V. T.'
                },
                'Para5': {
                    'Name': '',
                },
                'Para6': {
                    'Name': '',
                },
            }
        }
    if url == misc.api_sport:
        if not params.get('sport_id'):
            return [
                {
                    "sport": "Arm wrestling",
                    "sportid": "1"
                },
                {
                    "sport": "Badminton",
                    "sportid": "2"
                },
                {
                    "sport": "Basketball",
                    "sportid": "3"
                },
                {
                    "sport": "Weightlifting",
                    "sportid": "4"
                },
                {
                    "sport": "Freestyle wrestling",
                    "sportid": "5"
                },
                {
                    "sport": "Volleyball",
                    "sportid": "6"
                },
                {
                    "sport": "Gymnastics",
                    "sportid": "7"
                },
                {
                    "sport": "Greco-Roman wrestling",
                    "sportid": "8"
                },
                {
                    "sport": "Track and field",
                    "sportid": "9"
                },
                {
                    "sport": "Table tennis",
                    "sportid": "10"
                },
                {
                    "sport": "Swimming",
                    "sportid": "11"
                },
                {
                    "sport": "Sambo",
                    "sportid": "12"
                },
                {
                    "sport": "Rock climbing",
                    "sportid": "18"
                },
                {
                    "sport": "Special medical group",
                    "sportid": "13"
                },
                {
                    "sport": "Artistic gymnastics",
                    "sportid": "14"
                },
                {
                    "sport": "Tennis",
                    "sportid": "15"
                },
                {
                    "sport": "Tourism",
                    "sportid": "16"
                },
                {
                    "sport": "Football",
                    "sportid": "17"
                }
            ]
        else:
            return [
                {
                    "day": "Понеділок",
                    "prepod": "Alex W. B.",
                    "time": " 10.25",
                },
                {
                    "day": "Понеділок",
                    "prepod": "Alex W. B.",
                    "time": " 12.35",
                },
                {
                    "day": "Понеділок",
                    "prepod": "Alex W. B.",
                    "time": " 14.30",
                },
                {
                    "day": "Понеділок",
                    "prepod": "Emily L. K.",
                    "time": " 8.30",
                },
                {
                    "day": "Понеділок",
                    "prepod": "Emily L. K.",
                    "time": " 10.25",
                },
                {
                    "day": "Понеділок",
                    "prepod": "Olivia J. T.",
                    "time": " 12.35",
                },
                {
                    "day": "Понеділок",
                    "prepod": "Olivia J. T.",
                    "time": " 14.30",
                },
                {
                    "day": "Вівторок",
                    "prepod": "Emily L. K.",
                    "time": " 8.30",
                },
                {
                    "day": "Вівторок",
                    "prepod": "Emily L. K.",
                    "time": " 10.25",
                },
                {
                    "day": "Вівторок",
                    "prepod": "Olivia J. T.",
                    "time": " 10.25",
                },
                {
                    "day": "Вівторок",
                    "prepod": "Olivia J. T.",
                    "time": " 12.35",
                },
                {
                    "day": "Вівторок",
                    "prepod": "Olivia J. T.",
                    "time": " 14.30",
                },
                {
                    "day": "Вівторок",
                    "prepod": "Daniel S. M.",
                    "time": " 10.25",
                },
                {
                    "day": "Вівторок",
                    "prepod": "Daniel S. M.",
                    "time": " 12.35",
                },
                {
                    "day": "Вівторок",
                    "prepod": "Daniel S. M.",
                    "time": " 14.30",
                },
                {
                    "day": "Вівторок",
                    "prepod": "Sophia N. Q.",
                    "time": " 8.30",
                },
                {
                    "day": "Вівторок",
                    "prepod": "Sophia N. Q.",
                    "time": " 10.25",
                },
                {
                    "day": "Вівторок",
                    "prepod": "Sophia N. Q.",
                    "time": " 12.35",
                },
                {
                    "day": "Вівторок",
                    "prepod": "Michael R. D.",
                    "time": " 12.35",
                },
                {
                    "day": "Вівторок",
                    "prepod": "Michael R. D.",
                    "time": " 14.30",
                },
                {
                    "day": "Вівторок",
                    "prepod": "Michael R. D.",
                    "time": " 16.25",
                },
                {
                    "day": "Середа",
                    "prepod": "Alex W. B.",
                    "time": " 14.30",
                },
                {
                    "day": "Середа",
                    "prepod": "Alex W. B.",
                    "time": " 16.25",
                },
                {
                    "day": "Середа",
                    "prepod": "Emily L. K.",
                    "time": " 8.30",
                },
                {
                    "day": "Середа",
                    "prepod": "Emily L. K.",
                    "time": " 10.25",
                },
                {
                    "day": "Середа",
                    "prepod": "Daniel S. M.",
                    "time": " 14.30",
                },
                {
                    "day": "Середа",
                    "prepod": "Daniel S. M.",
                    "time": " 16.25",
                },
                {
                    "day": "Середа",
                    "prepod": "Sophia N. Q.",
                    "time": " 8.30",
                },
                {
                    "day": "Середа",
                    "prepod": "Sophia N. Q.",
                    "time": " 10.25",
                },
                {
                    "day": "Середа",
                    "prepod": "Michael R. D.",
                    "time": " 8.30",
                },
                {
                    "day": "Середа",
                    "prepod": "Michael R. D.",
                    "time": " 10.25",
                },
                {
                    "day": "Четверг",
                    "prepod": "Emily L. K.",
                    "time": " 8.30",
                },
                {
                    "day": "Четверг",
                    "prepod": "Emily L. K.",
                    "time": " 10.25",
                },
                {
                    "day": "Четверг",
                    "prepod": "Olivia J. T.",
                    "time": " 10.25",
                },
                {
                    "day": "Четверг",
                    "prepod": "Olivia J. T.",
                    "time": " 12.35",
                },
                {
                    "day": "Четверг",
                    "prepod": "Olivia J. T.",
                    "time": " 14.30",
                },
                {
                    "day": "Четверг",
                    "prepod": "Daniel S. M.",
                    "time": " 12.35",
                },
                {
                    "day": "Четверг",
                    "prepod": "Daniel S. M.",
                    "time": " 14.30",
                },
                {
                    "day": "Четверг",
                    "prepod": "Daniel S. M.",
                    "time": " 16.25",
                },
                {
                    "day": "Четверг",
                    "prepod": "Michael R. D.",
                    "time": " 8.30",
                },
                {
                    "day": "Четверг",
                    "prepod": "Michael R. D.",
                    "time": " 10.25",
                },
                {
                    "day": "Четверг",
                    "prepod": "Michael R. D.",
                    "time": " 12.35",
                },
                {
                    "day": "П`ятниця",
                    "prepod": "Emily L. K.",
                    "time": " 8.30",
                },
                {
                    "day": "П`ятниця",
                    "prepod": "Emily L. K.",
                    "time": " 10.25",
                },
                {
                    "day": "П`ятниця",
                    "prepod": "Olivia J. T.",
                    "time": " 12.35",
                },
                {
                    "day": "П`ятниця",
                    "prepod": "Olivia J. T.",
                    "time": " 14.30",
                },
                {
                    "day": "П`ятниця",
                    "prepod": "Olivia J. T.",
                    "time": " 14.30",
                },
                {
                    "day": "П`ятниця",
                    "prepod": "Daniel S. M.",
                    "time": " 8.30",
                },
                {
                    "day": "П`ятниця",
                    "prepod": "Daniel S. M.",
                    "time": " 10.25",
                }
            ]
