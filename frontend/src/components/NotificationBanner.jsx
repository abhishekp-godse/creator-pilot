import React from 'react';
import { AlertCircle, Clock, Zap, Flame, ShieldAlert } from 'lucide-react';

export function NotificationBanner({ notifications }) {
  if (!notifications || notifications.length === 0) return null;

  const getIcon = (type) => {
    switch (type) {
      case 'gap':
        return <AlertCircle className="w-5 h-5 text-amber-400" />;
      case 'best_time':
        return <Clock className="w-5 h-5 text-emerald-400" />;
      case 'streak':
        return <Flame className="w-5 h-5 text-rose-400" />;
      case 'burnout':
        return <ShieldAlert className="w-5 h-5 text-blue-400" />;
      default:
        return <Zap className="w-5 h-5 text-indigo-400" />;
    }
  };

  const getBorderColor = (urgency) => {
    switch (urgency) {
      case 'high':
        return 'border-amber-500/30 bg-amber-500/10 text-amber-200';
      case 'medium':
        return 'border-indigo-500/30 bg-indigo-500/10 text-indigo-200';
      default:
        return 'border-slate-700/60 bg-slate-800/40 text-slate-300';
    }
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-3 my-6">
      {notifications.map((n) => (
        <div
          key={n.id}
          className={`flex items-start gap-3 p-3.5 rounded-xl border backdrop-blur-sm transition hover:scale-[1.01] ${getBorderColor(
            n.urgency
          )}`}
        >
          <div className="mt-0.5 shrink-0">{getIcon(n.type)}</div>
          <div className="min-w-0">
            <div className="flex items-center justify-between gap-1">
              <h4 className="font-semibold text-xs text-white uppercase tracking-wider">{n.title}</h4>
              <span className="text-[10px] text-slate-400">{n.timestamp}</span>
            </div>
            <p className="text-xs mt-1 text-slate-300 leading-relaxed">{n.message}</p>
          </div>
        </div>
      ))}
    </div>
  );
}
