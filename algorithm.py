def trim(content, common_head_end_idx, common_foot_start_idx):
    return contet[common_head_end_idx, common_foot_start_idx]


def GetCommonHeader(ref_pages):
    headerList = []
    n = 0.7
    regex = ....  # constructed before
    headerList = re.match(regex, ref_pages)

    # find the first headerList match
    i = 0
    while i < len(ref_pages):
        headerList = re.match(regex, ref_pages[i])
        i += 1

        # edge case: can't find any header match, quit!
        if len(headerList) == 0 and i == len(ref_pages):
            return False
        elif len(headerList) == 1:
            if percent(header, ref_pages) >= n:
                return header

        # headerList should only contain 1 match, and this match should appear in
        # n of all pages.
        else:
            for header in headerList:
                if percent(header, ref_pages) >= n:
                    return header
        # at this step no common header is found in current header list,
        # go search for next header

    return False


def GetCommonFooter(ref_pages):
    # same as getCommonHeader except different regex value
    pass


def percent(header, ref_pages):
    header_exist_count = 0
    for page_content in ref_pages:
        if header in ref_pages:
            header_exist_count += 1
    return header_exist_count / len(ref_pages)


def addAnchor(ref_pages)
    for i in range(len(ref_pages)):
        ref_pages[i] = "$" + ref_pages[i] + "$"


def trim(page, common_head_end_idx, common_foot_start_idx):
    return page[common_head_end_idx:common_foot_start_idx]


def main():
    # add "$" anchar mark to beginning of page and end of page
    addAnchor(ref_pages)

    # Getting Common header and footers
    header = GetCommonHeader(ref_pages)
    footer = GetCommonFooter(ref_pages)

    for index in range(len(ref_pages)):
        page = ref_pages[index]
        page = trim(page, common_head_end_idx, common_foot_start_idx)
