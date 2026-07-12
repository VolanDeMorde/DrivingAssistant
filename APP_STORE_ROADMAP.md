# App Store Roadmap — Cyprus Driving Learner

---

## Recommended Language & Framework

### Best choice: **React Native** (with Expo)
**Why:**
- Your entire app is already JavaScript and HTML. React Native shares the same language — migration is a natural progression, not a rewrite.
- Expo wraps the complexity of iOS/Android build tooling so you can deploy to both stores from one codebase.
- Tailwind CSS has a React Native equivalent (NativeWind) so your visual style translates closely.
- Large community, excellent documentation, and free to start.

**Alternatives considered:**
| Option | Pros | Cons |
|---|---|---|
| Flutter (Dart) | High performance, great UI | New language to learn (Dart) |
| Native Swift/Kotlin | Best performance | Two separate codebases, high effort |
| Capacitor/Ionic | Wraps your existing HTML | App-store perception, performance limits |
| PWA only | Simplest path | Not listed in App Store/Google Play |

**Verdict:** React Native with Expo is the best ROI for a solo developer moving from web to mobile.

---

## Phase 1 — Foundation (Weeks 1–3)

### 1.1 Set up development environment
- [ ] Install Node.js (LTS)
- [ ] Install Expo CLI: `npm install -g expo-cli`
- [ ] Create project: `npx create-expo-app CyprusDrivingLearner`
- [ ] Install NativeWind for Tailwind-style CSS

### 1.2 Port core data
- [ ] Extract `sourcedSignSlugs`, `scenarios`, `allQuizQuestions` from `index.html` into separate JSON files
- [ ] Create `/data/signs.json`, `/data/scenarios.json`, `/data/quiz.json`
- [ ] Store sign images via S3 URLs (already sourced — no change needed)

### 1.3 Port core screens
- [ ] Road Signs screen (grid of image cards with flip animation)
- [ ] Quiz screen (progress bar, options, feedback)
- [ ] Scenarios screen (situation text, option buttons, feedback)
- [ ] Rules Guide screen (static content cards)

---

## Phase 2 — Mobile Polish (Weeks 4–6)

### 2.1 Navigation
- [ ] Install React Navigation
- [ ] Bottom tab bar with: Signs | Quiz | Scenarios | Guide
- [ ] Stack navigation within each tab

### 2.2 Mobile UX improvements
- [ ] Larger tap targets for all buttons (min 48x48pt)
- [ ] Swipe gesture to advance flashcards
- [ ] Haptic feedback on correct/incorrect answers
- [ ] Dark mode support

### 2.3 Offline capability
- [ ] Bundle all sign images locally (download once on first launch)
- [ ] AsyncStorage for quiz scores, scenario stats, weak topics
- [ ] Full offline functionality — no network required after install

---

## Phase 3 — App Store Preparation (Weeks 7–9)

### 3.1 Apple App Store (iOS)
- [ ] Enrol in Apple Developer Program ($99/year)
- [ ] Create App ID and provisioning profile in Apple Developer Portal
- [ ] Build with Expo EAS: `eas build --platform ios`
- [ ] Create App Store Connect listing:
  - App name, subtitle, description
  - Keywords (driving, Cyprus, road signs, test, learner)
  - Screenshots for iPhone 6.7" and iPad (required)
  - Privacy policy URL (required)
- [ ] Submit for App Review (typically 1–3 days)

### 3.2 Google Play Store (Android)
- [ ] Enrol in Google Play Developer ($25 one-time fee)
- [ ] Build with Expo EAS: `eas build --platform android`
- [ ] Create Play Console listing:
  - App content rating questionnaire
  - Privacy policy URL (required)
  - Screenshots for phone and 7" tablet
- [ ] Submit for review (typically 1–3 days for new accounts)

### 3.3 Legal requirements
- [ ] Write a Privacy Policy (free generators available at privacypolicygenerator.info)
- [ ] Host it on GitHub Pages (can use your existing repo)
- [ ] Add disclaimer that content is educational, not official legal advice

---

## Phase 4 — Growth Features (Post-launch)

- [ ] Push notifications for daily practice reminders
- [ ] User accounts and cloud sync (Firebase Auth + Firestore)
- [ ] Progress tracking across sessions with visual charts
- [ ] Timed mock exam mode (45 questions, 45 minutes)
- [ ] Multi-language support (Greek, Russian — common in Cyprus)
- [ ] In-app purchase for extended content or ad-free version

---

## Honest Assessment

**What is straightforward:**
- Porting the data and quiz logic is mechanical work — the hard thinking is already done.
- Expo removes most of the iOS/Android complexity.
- Your app is content-heavy, not compute-heavy, so React Native performs well.

**What will take real effort:**
- The App Store review process has strict guidelines. Educational apps must have a clear educational purpose statement.
- Apple requires a Privacy Policy and may reject apps with third-party image sources unless you have permission or host images yourself.
- Sign images currently load from a third-party S3 bucket (cysigns.online). For a production app, you should bundle or self-host the images to avoid dependency and potential copyright/availability issues. Contact cysigns.online for permission or recreate signs as SVG assets.
- Screenshot production takes more time than expected — plan for it.

**Realistic timeline to both stores:** 8–12 weeks working part-time.

---

## Resources

- Expo docs: https://docs.expo.dev
- React Navigation: https://reactnavigation.org
- NativeWind: https://www.nativewind.dev
- Apple Developer: https://developer.apple.com
- Google Play Console: https://play.google.com/console
- EAS Build: https://docs.expo.dev/build/introduction
