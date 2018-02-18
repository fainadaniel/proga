def kamal():
    with open("my.csv", encoding='utf-8') as f:
        kamall = {}
        for line in f:
            b = ((line.strip()).split(','))
            kamall.update({b[0]: b[1]})
    return kamall


def guess_word(kama):
        print('guess my word')
        for key in kama:
            print(key)
            a = input()
            m = 1
            while a.strip().lower() != kama[key].lower():
                print(m , 'try wrong.' 'try again')
                m += 1
                a = input()
            print('yes!')


def stihi():
    print ("Oh East is East and West is West\nAnd never the twain shall meet,\nTill Earth and Sky stand presently\nOn God's great judgement seat")


def well_done():
    print('  *       *  ****  *      *          * *      * *    *   *    ***** ')
    print('  *       *  *     *      *          *  *    *   *   **  *    *     ')
    print('  *   *   *  ***   *      *          *   *   *   *   * * *    ****  ')
    print('   * * * *   *     *      *          *   *   *   *   *  **    *     ')
    print('    *   *    ****  *****  *****      * **     * *    *   *    ***** ')


def main():
    stihi()
    guess_word(kamal())
    well_done()


main()
