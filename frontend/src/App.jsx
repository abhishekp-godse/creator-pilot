import React from 'react';
import { useCreatorPilot } from './controllers/useCreatorPilot';
import { Navbar } from './components/Navbar';
import { NotificationBanner } from './components/NotificationBanner';
import { MetricsOverview } from './components/MetricsOverview';
import { GrowthForecastChart } from './components/GrowthForecastChart';
import { ContentGapFinder } from './components/ContentGapFinder';
import { TrendIntelligence } from './components/TrendIntelligence';
import { IdeaVaultView } from './components/IdeaVaultView';
import { CollabMatcherView } from './components/CollabMatcherView';
import { AICoachModal } from './components/AICoachModal';
import { TitleScorerModal } from './components/TitleScorerModal';
import { WeeklyPlanModal } from './components/WeeklyPlanModal';
import { RefreshCw, Sparkles } from 'lucide-react';

export default function App() {
  const { state, actions } = useCreatorPilot();
  const {
    summary,
    notifications,
    forecast,
    gaps,
    videos,
    trends,
    ideas,
    collabs,
    loading,
    coachOpen,
    titleScorerOpen,
    initialScorerTitle,
    weeklyPlanOpen,
  } = state;

  return (
    <div className="min-h-screen bg-[#0b0f19] text-slate-100 flex flex-col font-['Plus_Jakarta_Sans',sans-serif]">
      {/* 1. Header View */}
      <Navbar
        onOpenCoach={() => actions.setCoachOpen(true)}
        onOpenTitleScorer={() => actions.openTitleScorerWith('')}
        onOpenWeeklyPlan={() => actions.setWeeklyPlanOpen(true)}
      />

      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 py-6">
        {/* Proactive Nudges & Inactivity Alert */}
        <NotificationBanner notifications={notifications} />

        {loading ? (
          <div className="flex flex-col items-center justify-center py-24 text-slate-400 gap-3">
            <RefreshCw className="w-8 h-8 animate-spin text-indigo-500" />
            <p className="text-sm">Ingesting channel telemetry & syncing AI Coach...</p>
          </div>
        ) : (
          <>
            {/* 2. Channel Profile, Growth Health Score & Monetization Tracker */}
            <MetricsOverview summary={summary} />

            {/* 3. 30-Day Predictive Growth Forecast (ML Prophet) */}
            <GrowthForecastChart forecast={forecast} />

            {/* 4. Idea Vault & AI Ranking (Real-World Creator Concept Backlog) */}
            <IdeaVaultView
              ideas={ideas}
              onAddIdea={actions.addIdea}
              onScoreTitle={actions.openTitleScorerWith}
            />

            {/* 5. Trend Intelligence Engine (Google Trends & Expiry Timer) */}
            <TrendIntelligence trends={trends} onSelectHook={actions.openTitleScorerWith} />

            {/* 6. Content Gap Finder & Retention Drop-Off Hook Analysis */}
            <ContentGapFinder
              gaps={gaps}
              videos={videos}
              onSelectTopic={actions.openTitleScorerWith}
            />

            {/* 7. Peer Creator Collab Matcher */}
            <CollabMatcherView collabs={collabs} />
          </>
        )}
      </main>

      {/* Floating Action Button for Voice Coach */}
      <button
        onClick={() => actions.setCoachOpen(true)}
        className="fixed bottom-6 right-6 z-30 flex items-center gap-2 px-5 py-3.5 rounded-full bg-gradient-to-r from-indigo-600 via-indigo-500 to-violet-600 text-white font-bold shadow-xl shadow-indigo-600/40 hover:scale-105 active:scale-95 transition"
      >
        <Sparkles className="w-5 h-5 text-indigo-200 animate-spin" />
        <span>Ask AI Coach</span>
      </button>

      {/* Interactive MVC Modals */}
      <AICoachModal isOpen={coachOpen} onClose={() => actions.setCoachOpen(false)} />
      <TitleScorerModal
        isOpen={titleScorerOpen}
        onClose={() => actions.setTitleScorerOpen(false)}
        initialTitle={initialScorerTitle}
      />
      <WeeklyPlanModal
        isOpen={weeklyPlanOpen}
        onClose={() => actions.setWeeklyPlanOpen(false)}
      />

      {/* Footer */}
      <footer className="border-t border-slate-800/80 py-6 text-center text-xs text-slate-500">
        CreatorPilot • Full-Stack MVC Architecture • Final Year Project
      </footer>
    </div>
  );
}
