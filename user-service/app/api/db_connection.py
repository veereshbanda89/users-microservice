def init_firestore():
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import firestore

    cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "cached-api-ecosystem",
  "private_key_id": "02a449d1fdee1345431a272cf2104ba2e37e5aa9",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDK/u1a4mZnEtQA\ndEQOP2Z209f+drTogyKqqU9RRj6eEGsVKbcsdjbfR/aK4M8kpctn10VyNfF955ab\nk3AW6N0sYykUKsvz+DhcNEvrCxqMu48v/m3AF+je29li924MeJZ75WfUlh9UPzOj\nDFX1jcsMSJ7nv2quPUEc7S7B0TAVtREb1/9SDCU5yWiK2xWBElmGy4OGnOOfHMYb\nxdKcbkxp65TDri2Rd2idhPV6AC/DP804dTwvtVtftNG4iP1IS3vFSD0WZgo3keSz\nQgHGeEF02qCCAnNeVkNGqw1SdbZpstD1AgfQNgXo9lghfJMMM+GS0FcCWRwFJohX\nbOkaAn+7AgMBAAECggEANuNMWZU6/CbWpRLK7hFNitbIIfmF/BKtNnkWRdMZDlNB\nKRVA/qguORxzuOSFjhK4V6kZEYMte445pnJszf0EBMMBMf9Ka3rT/nZziqfTc3cp\nheAlW9n7MPtAIebmXj/i7LhAZXZ8HSMDutQUkBNZckZWlTIoTdmpOAGX8Xc3Kb7y\nXKqbkAhHknTVndiyQeHaAenZzHAue1qNY4C1BoupcR/SjTJBB0KS0/FaK6Q7AzrU\nhy8AtyvSW6boY6xnMxC5GfpavgHN04/6T2ji3rphsiBMB9l6RQfzkMPLBsFn+uYz\nEzdt7QabQJFnYQGJsAKZ1oGyICbX6HN+QAbJLrFifQKBgQD9UhUaNEOANai6d1wh\nUQm4/Y6X+w9fZTngx5I5jLX+RXNrRmiv+DA78U+3MlwqF6kMxHUv72VTB3vpdIck\nU2sgG2Rws6jFZpn2JlRFVqEcD+M4bM2krX5olc8KmH3K5Y2gNQ0qhaMRQ3t/Zyu+\ndWvhvqzwiMtVXklcrQMed+MUxQKBgQDNJJR3u3hXiwm+uvwREK0HxkT6a7+/kJY1\nxhFdzEuS0TPxZKSU7gFrB+0uqcjlDPBupGNxCPel8T5U1IxC/Mefh9Uuua9o5gFn\nRHgbt6hkE+27ewoz6uhqc9iyvDdB6Mqwv1erZMIIba2GnWyB2IBrPLdhrkbkpVOq\nWrfmpxWKfwKBgBoHax+sKxtraBDw3siVmRgnBZXcODInJpFQMFg1eyXLYRauv2cF\na39dRkGerRWuJLKpJRlt0c18QWE1lgVHhQRhjCqAa2ENL9i5C4OsaRWHFGPh2ieH\npCt+6S0/if1lJO5HRTkPTjgh5PisUzRYwGMLwp1ckPgOnh8lr+Jbkzu5AoGAeW98\n/7+XBmOE2kX/7u4rL137+S2NbY3ejWh5YUgNOJTkpbHJB2w4pK4lhij1hjl5nlVr\nlD8VskKzfi3v9buDQ/l5hdZfcr4s+H98hhPa95sgcInuSTt2Z4W6MlvebgKq8aPi\n9s+HWMvsG7LWx6psoo5nk8hBqRoBA+f90uj3hGsCgYAJXl8wO7O2ZROm0/gyQL92\n+SBkrzrF1l1GwoMAZHmlPl8ylTT/zuyyr2+6BshSIIlVgsrzqIIxt9fFDO3gw9Gk\nbz9qV1NTLNy16FIL7uRenbCkdy2lKaf2qIxT1gqG8xEzEv4vhgEo8nPou6p1UgDW\nJbsRutcV3khF8RFKAFA0tA==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-in1wq@cached-api-ecosystem.iam.gserviceaccount.com",
  "client_id": "107381762162821876799",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-in1wq%40cached-api-ecosystem.iam.gserviceaccount.com"
}
)
    firebase_admin.initialize_app(cred)
    firestore_db = firestore.client()
    return firestore_db
