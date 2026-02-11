def count_valid_emails(emails):
    if not emails:
        return 0

    count = 0

    for email in emails:
        if isinstance(email, str) and "@" in email:
            count += 1

    return count
